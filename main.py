from config import open_weather_token
from pprint import pprint
import datetime
import requests


def get_weather(city, open_weather_token):
    try:
        #request
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru"
        )

        #json formatter

        data = r.json()
        # pprint(data)

        #parsing
        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        #output
        print(f"*** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ***\n"
              f"Погода в городе {city}\n"
              f"Температура: {temp}°C\n"
              f"Влажность: {humidity}%")


    #обработка ошибок
    except Exception as ex:
        print(ex)
        print("City name mistakes")

#main func
def main():
    city = input("Enter the city: ")
    get_weather(city, open_weather_token)

#enter point
if __name__ == '__main__':
    main()