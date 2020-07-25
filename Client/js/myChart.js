var ctx = document.getElementById('myChart').getContext("2d");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: '7 day average',
            data: [],
            backgroundColor: [
            ],
            borderColor: [
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainaspectratio: false,
        scales: {
            yAxes: [{
                ticks: {
                    max: 500,
                    beginAtZero: true
                }
            }]
        }
    }
});

function addData(chart, label, data) {  // is this being used??
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}
