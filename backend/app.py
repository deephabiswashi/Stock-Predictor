import os
import pickle
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# Get the absolute path to the project root.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define paths for templates and static folders.
TEMPLATES_DIR = os.path.join(BASE_DIR, 'frontend', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'frontend', 'static')

# Create the Flask app with explicit folder paths.
app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Define paths to the models and scaler (saved during training).
MODELS_DIR = os.path.join(BASE_DIR, 'models')
LINEAR_MODEL_PATH = os.path.join(MODELS_DIR, 'linear_regression_model.pkl')
LSTM_MODEL_PATH = os.path.join(MODELS_DIR, 'lstm_model.h5')
SCALER_PATH = os.path.join(MODELS_DIR, 'scaler.pkl')  # Make sure to save your scaler during training

# Load the Linear Regression model.
with open(LINEAR_MODEL_PATH, 'rb') as f:
    lr_model = pickle.load(f)

# Load the LSTM model.
lstm_model = load_model(LSTM_MODEL_PATH)

# Load the pre-fitted scaler.
with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.after_request
def add_header(response):
    # Disable caching for development.
    response.cache_control.no_store = True
    return response

@app.route('/predict', methods=['POST'])
def predict():
    """
    Expects JSON with features:
    {
      "Open": 19500,
      "High": 19600,
      "Low": 19400,
      "SharesTraded": 500000,
      "Turnover": 250
    }
    Returns JSON with 'lr_prediction' and 'lstm_prediction'.
    """
    data = request.get_json(force=True)
    
    # Extract features from the JSON.
    features = [
        data['Open'],
        data['High'],
        data['Low'],
        data['SharesTraded'],
        data['Turnover']
    ]
    
    # Convert to a NumPy array and reshape into a 2D array.
    features_array = np.array(features).reshape(1, -1)
    
    # Use the loaded scaler to transform the input (do not use fit_transform on a single row).
    features_array_scaled = scaler.transform(features_array)
    
    # Predict with the Linear Regression model.
    lr_prediction = lr_model.predict(features_array_scaled)[0]
    
    # Reshape for the LSTM (samples, timesteps, features).
    lstm_input = features_array_scaled.reshape(features_array_scaled.shape[0], 1, features_array_scaled.shape[1])
    lstm_prediction = lstm_model.predict(lstm_input)[0][0]
    
    result = {
        'lr_prediction': float(lr_prediction),
        'lstm_prediction': float(lstm_prediction)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
