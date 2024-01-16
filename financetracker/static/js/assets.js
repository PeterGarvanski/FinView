// Add Doughnut Chart data and options here// Add Doughnut Chart data and options here

var assetCtx = document.getElementById('asset-chart').getContext('2d');
var assetDoughnutChart = new Chart(assetCtx, {
    type: 'doughnut',
    data: {
        labels: ["House", "Stocks", "Crypto", "Cars"],
        datasets: [{
            data: [45, 27, 61, 36],
            borderColor: "#edf0f2",
            backgroundColor: ["#2d2354", "#edf0f2a8"],
            borderWidth: 5,
        }]
    },

    options: {
        display: false, // Set to false to hide the legend
    }
});
