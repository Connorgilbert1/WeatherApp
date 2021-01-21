import requests

from LIBS.openweather import OpenWeatherClient
from keys.api_arguments import CallType,Zip,Country,Unit


#Id to call API With
AppId = "db6cd39224db3858d8651580a22c603f"

#Making a Client Object
client = OpenWeatherClient(AppId)

#Calling a method in Client object. That will return a valid API call format
CALL = client.ClientCall(CallType.WEATHER, Zip.BELMONT, Country.NZ, Unit.METRIC)

#Calling the API

print(CALL)

