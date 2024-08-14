from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import requests

API_KEY = '0a2fc1de174d26bcfe7d5ba3682d04d9'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city_name):
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
        # Create a vertical layout
        layout = QVBoxLayout()

        # Set up the city input field
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.setFont(QFont('Arial', 14))
        layout.addWidget(self.city_input)

        # Set up the Get Weather button
        self.get_weather_button = QPushButton("Get Weather", self)
        self.get_weather_button.setFont(QFont('Arial', 14))
        self.get_weather_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.get_weather_button.clicked.connect(self.show_weather)
        layout.addWidget(self.get_weather_button)

        # Set up the result label
        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont('Arial', 12))
        self.result_label.setAlignment(Qt.AlignLeft)
        self.result_label.setStyleSheet("border: 1px solid #ddd; padding: 10px;")
        layout.addWidget(self.result_label)

        # Set up the main window
        self.setLayout(layout)
        self.setWindowTitle("Weather App")
        self.resize(400, 300)  # Set a default window size
        self.show()

    
    def show_weather(self):
        city_name = self.city_input.text()
        if city_name:
            weather_info = self.get_weather(city_name)
            self.result_label.setText(weather_info)
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")

if __name__ == '__main__':
    app = QApplication([])
    ex = WeatherApp()
    app.exec_()
