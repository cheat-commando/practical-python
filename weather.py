import requests

def get_weather_and_temps():
    api_key = '245e0a738889ec0817e9fb1e32e7e481'
    city = input("Name a city: ")

    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key

    request = requests.get(url)
    json = request.json()

    def kelvin_to_fahrenheit(kelvin):
        return round((kelvin-273)/5*9)

    temp = kelvin_to_fahrenheit(int(json['main']['temp']))
    temp_min = kelvin_to_fahrenheit(int(json.get('main').get('temp_min')))
    temp_max = kelvin_to_fahrenheit(int(json.get('main').get('temp_max')))

    return {
        "city": city,
        'description': json['weather'][0]['description'],
        'temp':temp,
        'temp_min': temp_min,
        'temp_max': temp_max
    }

def main():
    weather_dict = get_weather_and_temps()

    print("The current weather of " + weather_dict.get('city') + " is " + weather_dict.get('description') + '.')
    print("The current temperature in " + weather_dict.get('city') + " is", weather_dict.get('temp'), "degrees Fahrenheit.")
    print("The low for", weather_dict.get('city'), "today is", weather_dict.get('temp_min'), "degrees Fahrenheit.")
    print("The high for", weather_dict.get('city'), "today is", weather_dict.get('temp_max'), "degrees Fahrenheit.")

main()