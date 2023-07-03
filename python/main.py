import pandas as pd

# Veri setini CSV dosyasından oku
data_set = pd.read_csv('dataset/dataset.csv')

# Etiketleri ve verileri al
labels = data_set['label'].tolist()
data = data_set['value'].tolist()

# JavaScript kodunu oluştur
chart_code = """
var ctx = document.getElementById('barchart').getContext('2d');
var barchart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: %s,
        datasets: [{
            label: '# of Votes',
            data: %s,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
""" % (labels, data)

# JavaScript kodunu görüntüle
print(chart_code)

# JavaScript kodunu bir dosyaya yaz
with open('chart4.js', 'w') as file:
    file.write(chart_code)