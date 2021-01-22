#from keys.weather_keys import WeatherKeys


class WeatherParser:
    def __init__(self,api_data):
        self.api_data = api_data.json()


    def sky(self):
        return self.api_data['weather'][0]['description']

