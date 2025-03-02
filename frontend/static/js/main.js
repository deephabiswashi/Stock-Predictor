document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("predictionForm");
    const lrResult = document.getElementById("lrResult");
    const lstmResult = document.getElementById("lstmResult");
    const ctx = document.getElementById("predictionChart").getContext("2d");
  
    // Initialize Chart.js bar chart
    let predictionChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Linear Regression', 'LSTM'],
        datasets: [{
          label: 'Predicted Stock Price',
          data: [0, 0],
          backgroundColor: [
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)'
          ],
          borderColor: [
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  
    // Handle form submission
    form.addEventListener("submit", function(e) {
      e.preventDefault();
  
      // Retrieve user inputs
      const openVal = parseFloat(document.getElementById("open").value);
      const highVal = parseFloat(document.getElementById("high").value);
      const lowVal = parseFloat(document.getElementById("low").value);
      const sharesVal = parseFloat(document.getElementById("shares").value);
      const turnoverVal = parseFloat(document.getElementById("turnover").value);
  
      const data = {
        Open: openVal,
        High: highVal,
        Low: lowVal,
        SharesTraded: sharesVal,
        Turnover: turnoverVal
      };
  
      fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      })
      .then(response => {
        if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        return response.json();
      })
      .then(result => {
        // Update text-based results
        lrResult.textContent = "Linear Regression Prediction: " + result.lr_prediction.toFixed(2);
        lstmResult.textContent = "LSTM Prediction: " + result.lstm_prediction.toFixed(2);
  
        // Update chart with new predictions
        predictionChart.data.datasets[0].data = [
          result.lr_prediction,
          result.lstm_prediction
        ];
        predictionChart.update();
      })
      .catch(error => {
        console.error("Error:", error);
        lrResult.textContent = "Error: " + error;
        lstmResult.textContent = "";
      });
    });
  });
  