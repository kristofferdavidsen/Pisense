import json
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
key = os.getenv("JWT")

def encode(cels, fahr, id):
    payload: dict = {
            "tempCelsius": cels,
            "tempFahrenheit": fahr,
            "date": datetime.utcnow().isoformat(),
            "deviceId": id,
        }
    encoded_jwt = jwt.encode(payload, key)
    return encoded_jwt