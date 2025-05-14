// charts.js - Fixed version
document.addEventListener('DOMContentLoaded', function() {
    // 1. Get canvas element
    const ctx = document.getElementById('sensorChart');
    if (!ctx) return;

    // 2. Destroy previous chart if exists
    let myChart = ctx.chart;
    if (myChart) {
        myChart.destroy();
    }

    // 3. Create new chart
    ctx.chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Data',
                data: [],
                borderColor: '#36A2EB',
                borderWidth: 2
            }]
        }
    });

    // 4. Load data function
    function loadData() {
        fetch('/chart_data_jour/')
            .then(response => response.json())
            .then(data => {
                // Update chart data
                myChart = ctx.chart;
                myChart.data.labels = data.temps;
                myChart.data.datasets[0].data = data.temperature;
                myChart.update();
            })
            .catch(error => console.error('Error:', error));
    }

    // Initial load
    loadData();
});