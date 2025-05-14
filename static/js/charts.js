document.addEventListener('DOMContentLoaded', function() {
    // Set up time period buttons
    document.querySelectorAll('.time-period-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            // Update active button
            document.querySelectorAll('.time-period-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Fetch data for selected period
            fetchData(this.dataset.url);
        });
    });

    // Load initial data (today)
    const initialBtn = document.querySelector('.time-period-btn.active');
    if (initialBtn) {
        fetchData(initialBtn.dataset.url);
    }
});

function fetchData(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            updateChart(data);
            updateStats(data.temperature);
        })
        .catch(error => console.error('Error fetching data:', error));
}

function updateChart(data) {
    const chart = window.temperatureChart;

    // Format timestamps for Chart.js
    const formattedTimes = data.temps.map(time => new Date(time));

    // Update chart data
    chart.data.labels = formattedTimes;
    chart.data.datasets[0].data = data.temperature;

    // Update x-axis unit based on time range
    const timeRange = formattedTimes[formattedTimes.length - 1] - formattedTimes[0];
    const timeUnit = timeRange > 1000 * 60 * 60 * 24 * 7 ? 'day' :
                     timeRange > 1000 * 60 * 60 * 24 ? 'hour' : 'minute';

    chart.options.scales.x.time.unit = timeUnit;
    chart.update();
}

function updateStats(temperatureData) {
    if (temperatureData.length === 0) return;

    const sum = temperatureData.reduce((a, b) => a + b, 0);
    const avg = sum / temperatureData.length;
    const max = Math.max(...temperatureData);
    const min = Math.min(...temperatureData);

    document.getElementById('avg-temp').textContent = `${avg.toFixed(1)} °C`;
    document.getElementById('max-temp').textContent = `${max.toFixed(1)} °C`;
    document.getElementById('min-temp').textContent = `${min.toFixed(1)} °C`;
}