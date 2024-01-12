// Add Doughnut Chart data and options here
var ctx = document.getElementById('doughnutChart').getContext('2d');
var doughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [33, 67, 100],
            backgroundColor: ["#edf0f221", "#edf0f2a8", "#ffffff00"],
            borderColor: ["#edf0f2", "#edf0f2", "#ffffff00"],
            borderWidth: 4,
        }]
    },
    options: {
        cutoutPercentage: 60,
    }
});


var ctx = document.getElementById('doughnutChart2').getContext('2d');
var doughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [7611, 2389, 10000],
            backgroundColor: ["#edf0f221", "#edf0f2a8", "#ffffff00"],
            borderColor: ["#edf0f2", "#edf0f2", "#ffffff00"],
            borderWidth: 4,
        }]
    },
    options: {
        cutoutPercentage: 60,
    }
});