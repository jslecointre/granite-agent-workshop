from __future__ import annotations

import requests
from ibm_granite_community.notebook_utils import get_env_var
from langchain_core.utils.utils import convert_to_secret_str

AV_STOCK_API_KEY = convert_to_secret_str(get_env_var("AV_STOCK_API_KEY", "unset"))
WEATHER_API_KEY = convert_to_secret_str(get_env_var("WEATHER_API_KEY", "unset"))


def get_stock_price(ticker: str, date: str) -> dict:
    """
    Retrieves the lowest and highest stock prices for a given ticker and date.

    Args:
        ticker: The stock ticker symbol, for example, "IBM".
        date: The date in "YYYY-MM-DD" format for which you want to get stock prices.

    Returns:
        A dictionary containing the low and high stock prices on the given date.
    """
    print(f"Getting stock price for {ticker} on {date}")

    apikey = AV_STOCK_API_KEY.get_secret_value()
    if apikey == "unset":
        print("No API key present; using a fixed, predetermined value for demonstration purposes")
        return {
            "low": "245.4500",
            "high": "249.0300"
        }

    try:
        stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={apikey}"
        stock_data = requests.get(stock_url)
        data = stock_data.json()
        stock_low = data["Time Series (Daily)"][date]["3. low"]
        stock_high = data["Time Series (Daily)"][date]["2. high"]
        return {
            "low": stock_low,
            "high": stock_high
        }
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return {
            "low": "none",
            "high": "none"
        }


def get_current_weather(location: str) -> dict:
    """
    Fetches the current weather for a given location (default: San Francisco).

    Args:
        location: The name of the city for which to retrieve the weather information.

    Returns:
        A dictionary containing weather information such as temperature in celsius, weather description, and humidity.
    """
    print(f"Getting current weather for {location}")
    apikey = WEATHER_API_KEY.get_secret_value()
    if apikey == "unset":
        print("No API key present; using a fixed, predetermined value for demonstration purposes")
        return {
            "description": "thunderstorms",
            "temperature": 25.3,
            "humidity": 94
        }

    try:
        # API request to fetch weather data
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}&units=metric"
        weather_data = requests.get(weather_url)
        data = weather_data.json()
        # Extracting relevant weather details
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Returning weather details
        return {
            "description": weather_description,
            "temperature": temperature,
            "humidity": humidity
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return {
            "description": "none",
            "temperature": "none",
            "humidity": "none"
        }
