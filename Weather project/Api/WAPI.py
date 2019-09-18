import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=3b9aef642e2c6ee5ef9e9d6cbf2d41ea&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['main']
print(format_add)
