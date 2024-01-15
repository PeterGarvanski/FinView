// Add Doughnut Chart data and options here

var savingsCtx = document.getElementById('savings-chart').getContext('2d');
var savingsDoughnutChart = new Chart(savingsCtx, {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [33, 67, 100],
            backgroundColor: ["#2d2354", "#edf0f2a8", "#ffffff00"],
            borderColor: ["#edf0f2", "#edf0f2", "#ffffff00"],
            borderWidth: 4,
        }]
    },
    options: {
        cutoutPercentage: 60,
    }
});

var netWorthCtx = document.getElementById('net-worth-chart').getContext('2d');
var netWorthDoughnutChart = new Chart(netWorthCtx, {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [7611, 2389, 10000],
            backgroundColor: ["#2d2354", "#edf0f2a8", "#ffffff00"],
            borderColor: ["#edf0f2", "#edf0f2", "#ffffff00"],
            borderWidth: 4,
        }]
    },
    options: {
        cutoutPercentage: 60,
    }
});