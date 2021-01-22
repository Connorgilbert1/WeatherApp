import requests

from LIBS.openweather import OpenWeatherClient
from keys.WeatherData import WeatherData
from parsers.weather_parser import WeatherParser


#Id to call API With
AppId = "db6cd39224db3858d8651580a22c603f"

#Making a Client Object
client = OpenWeatherClient(AppId)

data = WeatherData()
calltype = data.getCallTypes()[0]
zip = data.getZips()[0]["belmont"]
country = data.getCountries()[0]
unit = data.getUnits()[0]

#Calling a method in Client object. That will return a valid API call format
CALL = client.ClientCall(calltype, zip, country, unit)

#print(CALL)
api_call = requests.get(CALL)

print(CALL)


Parsed = WeatherParser(api_call)

print(Parsed.sky())



#  failed attempt to make proccess into a class
#
# class Call:
#     def __init__(self):
#
#
#     def caller(self,CallType,Zip,Country,Unit):
#         Call = client.ClientCall(CallTypes.CallType, Zips.Zip, Countries.Country, Units.Unit)
#         return Call


