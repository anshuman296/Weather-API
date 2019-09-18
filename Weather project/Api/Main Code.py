import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=3b9aef642e2c6ee5ef9e9d6cbf2d41ea&q='
city = input('City Name :')
url = api_address + city
response = requests.get(url)
x = response.json()


if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]


    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")