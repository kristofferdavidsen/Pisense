import jwt
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
key = os.getenv("JWT_DEVICE")

def encodeTemp(cels, fahr, id):
    payload = {
            "tempCelsius": cels,
            "tempFahrenheit": fahr,
            "date": datetime.utcnow().isoformat(),
            "deviceId": id,
        }
    encoded_jwt = jwt.encode(payload, key)
    return encoded_jwt

def encodeHum(hum, id):
    payload = {
        "humidity": hum,
        "date": datetime.utcnow().isoformat(),
        "deviceId": id,
    }
    encoded_jwt = jwt.encode(payload, key)
    return encoded_jwt