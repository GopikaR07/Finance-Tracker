const ctx = document.getElementById('spendingChart').getContext('2d');
const spendingChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Food', 'Travel', 'Education', 'Other'],
        datasets: [{
            label: 'Spending by Category',
            data: [300, 200, 100, 400], // Replace with dynamic data
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']
        }]
    }
});
