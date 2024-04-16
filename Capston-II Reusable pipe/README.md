# ForecastWizard: A Friendly Forecast Tool

ForecastWizard is a user-friendly web application designed to assist users in forecasting sales data using the AutoSARIMAX model. It provides a simple interface for users to upload their CSV files containing date and sales columns, and it automatically identifies the best model parameters for forecasting.

## Features

- Upload CSV files containing date and sales data.
- Automatically determine the best model parameters using the AutoSARIMAX model.
- Display the forecasted sales data for the next 10 instances.
- Simple and intuitive user interface.

## Contributors

- [Mohammad Muneeb Nawal](https://github.com/muneeb-nawal) (0811582)
- [Venkat Sai Akash Cheerla](https://github.com/venkatsaia448) (0815019)
- [Sally Rana](https://github.com/sally-rana) (0812554)
- [Shikha Sharma](https://github.com/shikha-sharma10) (0803141)
- [Dhairya Nagpal](https://github.com/dhairyanagpal) (0823373)

## Usage

1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Access the application in your web browser at `http://localhost:5000`.
5. Upload your CSV file containing date and sales data.
6. View the forecasted sales data and the best model parameters.

## Technologies Used

- Python
- Flask
- pmdarima (AutoSARIMAX model)
- HTML/CSS
- JavaScript (jQuery)

## Screenshots

![Forecast Wizard](Capston-II%20Reusable%20pipe/Images/ForecastWizard.png "Forecast Wizard")

## Requirements

- Flask==2.0.2
- pmdarima==1.8.2

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
