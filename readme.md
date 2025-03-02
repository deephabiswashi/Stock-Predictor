<h1 style="color: #2F4F4F; text-align:center;">
  <b>Stock Price Prediction using Machine Learning</b>
</h1>

<p style="text-align:center;">
  <em>Predict stock prices using ML models like LSTM and Linear Regression</em>
</p>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">1. Overview</h2>

<p>
  This project aims to predict stock prices using Machine Learning techniques. It leverages historical market data and applies models such as 
  <strong>Long Short-Term Memory (LSTM)</strong> and <strong>Linear Regression</strong> for forecasting stock prices. Key features include:
</p>

<ul>
  <li><strong>Data Processing:</strong> Reads stock market data and applies preprocessing techniques.</li>
  <li><strong>Feature Scaling:</strong> Uses MinMaxScaler for better model performance.</li>
  <li><strong>Model Training:</strong> Implements LSTM for time-series forecasting and Linear Regression for trend prediction.</li>
  <li><strong>Web Interface:</strong> A frontend to visualize predictions using HTML, CSS, and JavaScript.</li>
</ul>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">2. Project Structure</h2>

<pre>
Stock-Price-Prediction/
├── backend/
│   ├── app.py                # Flask backend for model inference
│   ├── requirements.txt      # Python dependencies
│
├── data/
│   ├── NIFTY 500-02-01-2024-to-02-01-2025.csv  # Stock market dataset
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css      # Frontend styling
│   │   ├── js/
│   │   │   ├── main.js        # JavaScript for interactivity
│   ├── templates/
│   │   ├── index.html         # Main webpage template
│
├── models/
│   ├── linear_regression_model.pkl  # Trained Linear Regression model
│   ├── lstm_model.h5                # Trained LSTM model
│   ├── scaler.pkl                    # Scaler used for data normalization
│
├── notebooks/                         # Jupyter Notebooks (if any)
│
├── screenshots/
│   ├── homepage.png
│   ├── results1.png
│   ├── results2.png
│
├── venv1/                             # Virtual environment (optional)
├── README.md                          # Project documentation
└── .gitignore                         # Git ignore rules
</pre>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">3. Installation</h2>

<ol>
  <li>
    <strong>Clone this repository:</strong>
    <pre><code>git clone https://github.com/deephabiswashi/Stock-Predictor.git</code></pre>
  </li>
  <li>
    <strong>Create and activate a virtual environment (optional):</strong>
    <pre><code>python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
</code></pre>
  </li>
  <li>
    <strong>Install dependencies:</strong>
    <pre><code>pip install -r requirements.txt
</code></pre>
  </li>
</ol>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">4. Usage</h2>

<ol>
  <li><strong>Run the Flask backend:</strong>
    <pre><code>python backend/app.py</code></pre>
  </li>
  <li><strong>Access the web interface:</strong>
    <pre><code>Open http://127.0.0.1:5000 in your browser</code></pre>
  </li>
  <li><strong>View predictions:</strong> Upload stock data and see LSTM & Linear Regression predictions.</li>
</ol>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

## 🔹 Demo Video

[![Watch the video](https://img.youtube.com/vi/YeT7VT5CZto/0.jpg)](https://youtu.be/YeT7VT5CZto)

🔗 Click the image above to watch the demo on YouTube.

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

## 🔹 Screenshots

### 🏠 Homepage
![Homepage](screenshots/homepage.png)

### 📈 Prediction Results 1
![Results 1](screenshots/results1.png)

### 📊 Prediction Results 2
![Results 2](screenshots/results2.png)

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

## 🔹 Dataset Source

This project uses historical stock price data from **[NSE (National Stock Exchange of India)](https://www.nseindia.com/reports-indices-historical-index-data)**.

📌 **Credit:** All rights to the dataset belong to NSE India. The dataset was sourced from their official **historical index data** section.

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">5. Contributing</h2>

<p>
  Contributions are welcome! Feel free to open issues or submit pull requests.
</p>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">6. License</h2>

<p>
  This project is licensed under the <strong>MIT License</strong>.
</p>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<p style="text-align:center;">
  <em>Made with ❤️ by Deep</em>
</p>
