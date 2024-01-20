document.addEventListener('DOMContentLoaded', function () {
    var dataContainer = document.getElementById('dashboard-data-container');
    var jsonData = JSON.parse(dataContainer.getAttribute('data'));

    if (jsonData.net_worth_goal <= jsonData.net_worth) {
        jsonData.net_worth = jsonData.net_worth_goal
    }

    if (jsonData.savings_goal <= jsonData.savings) {
        jsonData.savings = jsonData.savings_goal
    }

    var savingsCtx = document.getElementById("savings-chart").getContext("2d");
    new Chart(savingsCtx, {
        type: "doughnut",
        data: {
            datasets: [{
                data: [(jsonData.savings_goal - jsonData.savings), jsonData.savings, (jsonData.savings_goal)],
                backgroundColor: ["#2d2354", "#edf0f2a8", "#ffffff00"],
                borderColor: ["#edf0f2", "#edf0f2", "#ffffff00"],
                borderWidth: 4,
            }]
        },
        options: {
            cutoutPercentage: 60,
        }
    });

    var netWorthCtx = document.getElementById("net-worth-chart").getContext("2d");
    new Chart(netWorthCtx, {
        type: "doughnut",
        data: {
            datasets: [{
                data: [(jsonData.net_worth_goal - jsonData.net_worth), jsonData.net_worth, jsonData.net_worth_goal],
                backgroundColor: ["#2d2354", "#edf0f2a8", "#ffffff00"],
                borderColor: ["#edf0f2", "#edf0f2", "#ffffff00"],
                borderWidth: 4,
            }]
        },
        options: {
            cutoutPercentage: 60,
        }
    });

});