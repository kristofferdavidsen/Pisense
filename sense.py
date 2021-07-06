from sense_hat import SenseHat

sense = SenseHat()

def readCelsius():
    tempCelsius = sense.get_temperature()
    return tempCelsius

def readFahrenheit(tempCelsius):
    tempFahrenheit = tempCelsius * 1.8 + 32
    return tempFahrenheit

def readHumidity():
    hum = sense.get_humidity()
    return hum