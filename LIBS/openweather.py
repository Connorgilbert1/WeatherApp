

class OpenWeatherClient:

    # property in class for base url
    BASE_URL = "https://api.openweathermap.org/data/2.5"


    # creating self object to store app id in

    def __init__(self,AppId):
        self.AppId = AppId

    #method to create an API call (url format)

    def ClientCall(self,CallType,Zip,Country,Unit):
        return f"{self.BASE_URL}/{CallType}?zip={str(Zip)},{Country}&units={Unit}&appid={self.AppId}"


