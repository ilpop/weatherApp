# Weather App

## Overview

The Weather App is a simple desktop application built using PyQt5 and Python. It allows users to enter a city name and retrieve current weather information for that city using the [OpenWeatherMap](https://home.openweathermap.org/) API.

## Features

- Enter a city name to get current weather details.
- Displays temperature, humidity, pressure, weather description, and wind speed.
- Modern UI with a responsive layout.

## Installation

### Prerequisites

Ensure you have Python 3.7 or later installed on your system.

### Setting Up the Environment

1. **Clone the Repository**

    ```
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. **Create and Activate a Virtual Environment**

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```

4. **Obtain an API Key** (This phase can be skipped)

   - Sign up for an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
   - Replace `your_openweathermap_api_key` in `weather_app.py` with your actual API key.

## Running the Application

To start the application:

  ```
  python3 weather_app.py
  ```


## Usage

Enter City Name
Type the name of the city you want to get the weather for in the input field.

 ## Get Weather

Click the "Get Weather" button to fetch and display the weather information for the entered city.

## Run Tests

  ```
  pip install pytest
  pytest
  ```

## Customization

You can customize the appearance and functionality of the app by modifying the following:

Fonts and Colors: Change the styles in the setStyleSheet method in weather_app.py.
Layout and Widgets: Adjust the layout and widgets in the initUI method as needed.

## Troubleshooting

No Weather Information Displayed:
Ensure your API key is correctly set in weather_app.py.
Verify your internet connection.

Application Not Starting:
Check for any missing dependencies or errors in the installation process.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

PyQt5 Documentation
OpenWeatherMap API

## Contact

For questions or feedback, please contact ilkka.ihalainen@gmail.com.

