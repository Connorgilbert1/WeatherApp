import requests

class OpenWeatherClient:

    BASE_URL = "https://api.openweathermap.org/data/2.5"

    def __init__(self,AppId):
        self.AppId = AppId



    def ClientCall(self,CallType,Zip,Country,Unit):
        return f"{self.BASE_URL}/{CallType}?zip={Zip},{Country}&units={Unit}&appid={self.AppId}"


