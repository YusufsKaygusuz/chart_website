<h1 align="center">KYGSZ || Chart</h1>

<p align="center">
    <img src="https://img.shields.io/badge/made%20with-HTML-red" alt="Made with HTML">
    <img src="https://img.shields.io/badge/made%20with-CSS-blue" alt="Made with CSS">
</p>

<p align="center">
    <strong>Responsive chart templates built using Chart.js library.</strong>
</p>

<p align="center">
    <img src="https://asset.brandfetch.io/idFdo8ulhr/idzj34qGQm.png" alt="Screenshot" style="width:15%; ">
</p>

## Using

1) Install `Python` packages. 

        pip install pandas

2) Open the `dataset.csv` file and update your data.

        label,value
        Red,12
        Blue,19
        Yellow,3
        Green,5
        Purple,2
        Orange,3


3) Update your dataset using the relevant tags and values. Generate the JavaScript code by running `main.py`.

       python main.py


4) This step reads the data from the dataset.csv file using the pandas library on the Python side and generates the JavaScript code. The generated JavaScript code is written to the chart4.js file. Open the `index.html` file in a web browser to view the results.

        double-click index.html

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/username/chart_website.git


1. Open the index.html file in your web browser.

## Usage
The index.html file contains a sample structure for displaying three types of charts: bar chart, doughnut chart, and polar area chart. The charts are created using the Chart.js library.

To customize the charts or add your own data, you can modify the JavaScript files in the script directory:

- chart1.js for the bar chart
- chart2.js for the doughnut chart
- chart3.js for the polar area chart

<p>Feel free to explore the provided CSS file style.css to make any styling adjustments.</p>

Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).

Note: Note that you need to replace the  `https://github.com/username/repo-name` link with the URL of the actual GitHub repository.
Also, you need to replace `your-demo-link` with the URL of the live demo.
