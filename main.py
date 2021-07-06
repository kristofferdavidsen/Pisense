# TODO: Implement functionality for loading user settings from db.
# This way it's possible to control timers, name, location etc.

import time as t
from sense import readCelsius, readFahrenheit, readHumidity
from encode import encodeHum, encodeTemp
from db import postDB

def main():
    while (True):
        celsius = readCelsius()
        fahrenheit = readFahrenheit(celsius)
        hum = readHumidity()
        encodedTemp = encodeTemp(celsius, fahrenheit, "kristoffer_1")
        encodedHum = encodeHum(hum, "kristoffer_1")
        resTemp = postDB("temperature", encodedTemp)
        print(resTemp)
        resHum = postDB("humidity", encodedHum)
        print(resHum)
        t.sleep(3600)

if __name__ == "__main__":
    main()