from sense_hat import SenseHat
import requests

# https://github.com/kristofferdavidsen/Pinterface/tree/main/interfaces
# https://2.python-requests.org/en/master/user/quickstart/#make-a-request
# https://pythonhosted.org/sense-hat/

sense = SenseHat()
acelsius = sense.get_temperature_from_pressure()
