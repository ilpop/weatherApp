from dotenv import load_dotenv
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import requests


load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY') 
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):  # Now outside the class
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()

        weather_data = response.json()

        if weather_data['cod'] == 200:
            main = weather_data['main']
            wind = weather_data['wind']
            weather_description = weather_data['weather'][0]['description']

            weather_info = (
                f"City: {city_name}\n"
                f"Temperature: {main['temp']}°C\n"
                f"Humidity: {main['humidity']}%\n"
                f"Pressure: {main['pressure']} hPa\n"
                f"Weather: {weather_description.capitalize()}\n"
                f"Wind Speed: {wind['speed']} m/s"
            )
            return weather_info
        else:
            return f"City {city_name} not found."

    except requests.exceptions.HTTPError as http_err:
        return f"City {city_name} not found."
    except Exception as err:
        return f"An error occurred: {err}"

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        font = QFont('Roboto', 18)  # Font family and size
        self.setFont(font)  # Apply to the entire widget

        # Set the color palette
        self.setStyleSheet("""
            QWidget {
                background-color: #F0F0F0; /* Light gray background */
                color: #333333; /* Dark gray text */
            }
            QLineEdit {
                background-color: #FFFFFF; /* White background for input */
                border: 1px solid #CCCCCC; /* Light gray border */
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #007BFF; /* Blue button background */
                color: #FFFFFF; /* White text */
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
                font-size: 14px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #0056b3; /* Darker blue on hover */
            }
            QLabel {
                margin: 10px;
            }
        """)

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter city name (e.g., Helsinki or London)")
        layout.addWidget(self.city_input)

        # Horizontal layout for buttons
        button_layout = QVBoxLayout()

        # Get weather button
        self.get_weather_button = QPushButton("Get Weather", self)
        self.get_weather_button.clicked.connect(self.show_weather)
        button_layout.addWidget(self.get_weather_button)

        # Exit button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)  # Connect to close method
        button_layout.addWidget(self.exit_button)

        layout.addLayout(button_layout)

        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle("Weather App")
        self.resize(400, 300)  # Set a reasonable default window size
        self.show()

    
    def show_weather(self):
        city_name = self.city_input.text()
        if city_name:
            weather_info = get_weather(city_name)  # Call standalone get_weather
            self.result_label.setText(weather_info)
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")

if __name__ == '__main__':
    app = QApplication([])
    ex = WeatherApp()
    app.exec_()
