document.addEventListener('DOMContentLoaded', (event) => {
    const onButton = document.getElementById('onButton');
    const offButton = document.getElementById('offButton');
    const logButton = document.getElementById('logButton');
    const dataStream = document.getElementById('dataStream');
    const logs = document.getElementById('logs');

    let dataStreamInterval;
    let logsInterval;
    let orionActive = false;

    onButton.addEventListener('click', () => {
        orionActive = true;
        dataStream.innerHTML = '<p>Data stream will appear here...</p>';
        if (dataStreamInterval) {
            clearInterval(dataStreamInterval);
        }
        dataStreamInterval = setInterval(() => {
            if (orionActive) {
                fetchDataStream();
            }
        }, 1000);
    });

    offButton.addEventListener('click', () => {
        orionActive = false;
        clearInterval(dataStreamInterval);
        dataStream.innerHTML = '<p>Data stream stopped.</p>';
    });

    logButton.addEventListener('click', () => {
        if (logsInterval) {
            clearInterval(logsInterval);
        }
        logsInterval = setInterval(fetchLogs, 1000);
    });

    function fetchDataStream() {
        // Simulate fetching data from the backend
        const data = `Data part: ${Math.random().toFixed(5)}`;
        const dataElement = document.createElement('p');
        dataElement.textContent = data;
        dataStream.appendChild(dataElement);
        dataStream.scrollTop = dataStream.scrollHeight;
    }

    function fetchLogs() {
        // Simulate fetching logs from the backend
        const log = `Log entry: ${new Date().toLocaleTimeString()}`;
        const logElement = document.createElement('p');
        logElement.textContent = log;
        logs.appendChild(logElement);
        logs.scrollTop = logs.scrollHeight;
    }
});

document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('dataGraph').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line', // Example: line chart

        // The data for our dataset
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'Demo Data',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [0, 10, 5, 2, 20, 30, 45]
            }]
        },

        // Configuration options
        options: {}
    });
});

