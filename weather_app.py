import requests

API_KEY = "YOUR_API_KEY_HERE"

city = input("Enter city name: ").strip()

if city == "":
    print("City name cannot be empty.")
else:
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n----- Weather Information -----")
            print("City:", data["name"])
            print("Temperature:", temperature_c, "°C")
            print("Temperature:", round(temperature_f, 2), "°F")
            print("Humidity:", humidity, "%")
            print("Weather Condition:", condition.title())
            print("Wind Speed:", wind_speed, "m/s")

        elif response.status_code == 404:
            print("Error: City not found.")

        elif response.status_code == 401:
            print("Error: Invalid API key.")

        else:
            print("Error: Unable to get weather information.")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Please check your internet connection.")

    except requests.exceptions.RequestException:
        print("Error: Something went wrong.")                                                                                                                                            give the readme for this coding
-
