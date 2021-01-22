# All the data you can extract from openweather api by metrics
 #init is a constructor
class WeatherData:
    def __init__(self):
        self.callTypes = ["weather", "box", "find"]
        self.zips = [{"belmont": "0622"}, {"devonport": "1100"}]
        self.countries = ["NZ", "US"]
        self.units = ["metric", "imperial"]

    def getCallTypes(self):
        return self.callTypes

    def getZips(self):
        return self.zips

    def getCountries(self):
        return self.countries

    def getUnits(self):
        return self.units

