class Weather():

    api_key = "66bea5a2c8348fa1ff3a7c99865ed684"
    city_name = ""
    weather_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api_key + "&q=" + city_name + "&units=metric"
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast?" + "appid=" + api_key + "&q=" + city_name + "&units=metric"

    def __init__(self, city_name):
        self.city_name = city_name
        self.weather_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + self.api_key + "&q=" + self.city_name + "&units=metric"
        self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast?" + "appid=" + self.api_key + "&q=" + self.city_name + "&units=metric"


    def getWeatherToday(self):
        import requests
        import json

        weather = requests.get(self.weather_url)
        a = weather.json()

        forecast = requests.get(self.forecast_url)
        x = forecast.json()

        if a["cod"] != "404" and x["cod"] != "404":
            # Current weather
            print(a)
            weather_description = a["weather"][0]["description"]
            wind_speed = a["wind"]["speed"]
            clouds = a["clouds"]["all"]

            b = a["main"]
            temperature = int(b["temp"])  # int() used to round
            feels_like_temp = int(b["feels_like"])
            min_temp = int(b["temp_min"])
            max_temp = int(b["temp_max"])
            humidity = b["humidity"]

        return [temperature, feels_like_temp, min_temp, max_temp, humidity, weather_description, wind_speed, clouds]

        # print("Today's Weather: " +
        #     "\n  Description = " + weather_description +
        #     "\n  Temperature = " + str(temperature) + "°C" +
        #     "\n  Feels like = " + str(feels_like_temp) + "°C" +
        #     "\n  Minimum temperature = " + str(min_temp) + "°C" +
        #     "\n  Maximum temperature = " + str(max_temp) + "°C" +
        #     "\n  Humidity = " + str(humidity) + "%" +
        #     "\n  Winds Speed = " + str(wind_speed) + " m/s" +
        #     "\n  Cloudiness = " + str(clouds) + "%\n")

    def get5DayWeather(self):
        import requests
        import json

        forecast = requests.get(self.forecast_url)
        x = forecast.json()
        forecastList = x["list"]
        fiveDayForecast = []  # format: [[day1Date, day1Weather, day1Temp, day1Humidity], [day2Date, day2Weather, day2Temp, day2Humidity]...]

        i = 0
        while i < 40:  # 5 day forecast every 3 hours (40 entries of data)
            dt_txt = forecastList[i]["dt_txt"]  # format: 2020-07-05 03:00:00

            if dt_txt[11:13] == "12":
                forecastDate = dt_txt[:10]
                forecastDescription = forecastList[i]["weather"][0]["description"]
                forecastTemp = int(forecastList[i]["main"]["temp"])
                forecastHumidity = forecastList[i]["main"]["humidity"]
                fiveDayForecast.append([forecastDate, forecastDescription, forecastTemp, forecastHumidity])

                i += 8  # straight to next 12 noon for consistency
            else:
                i += 1

        return fiveDayForecast
