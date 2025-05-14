document.addEventListener('DOMContentLoaded', function() {
    // Auto-submit filter form
    const filterSelect = document.getElementById('mon_select');
    if (filterSelect) {
        filterSelect.addEventListener('change', function() {
            document.getElementById('filter-form').submit();
        });
    }

    // CSV Export
    const csvButton = document.getElementById('csv');
    if (csvButton) {
        csvButton.addEventListener('click', function() {
            fetch('/download_csv/')
                .then(response => response.blob())
                .then(blob => {
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'sensor_data.csv';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                })
                .catch(error => {
                    console.error('Error downloading CSV:', error);
                });
        });
    }

    // Auto-refresh every 60 seconds
    setTimeout(function() {
        location.reload();
    }, 60000);
});