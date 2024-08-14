# test_weather.py

import pytest
import requests
from weather_app import get_weather  # Now this should be importable

def test_get_weather_success(monkeypatch):
    def mock_get(url):
        class MockResponse:
            def json(self):
                return {
                    'cod': 200,
                    'main': {'temp': 25, 'humidity': 80, 'pressure': 1013},
                    'wind': {'speed': 5},
                    'weather': [{'description': 'clear sky'}]
                }
            def raise_for_status(self):
                pass
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    result = get_weather('London')
    expected = (
        "City: London\n"
        "Temperature: 25°C\n"
        "Humidity: 80%\n"
        "Pressure: 1013 hPa\n"
        "Weather: Clear sky\n"
        "Wind Speed: 5 m/s"
    )
    assert result == expected

def test_get_weather_failure(monkeypatch):
    def mock_get(url):
        class MockResponse:
            def json(self):
                return {'cod': 404}
            def raise_for_status(self):
                raise requests.exceptions.HTTPError("Not Found")
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    result = get_weather('InvalidCity')
    assert result == "City InvalidCity not found."

