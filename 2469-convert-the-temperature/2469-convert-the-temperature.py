class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        farenheit = celsius * 1.8 + 32

        return [kelvin, farenheit]
        