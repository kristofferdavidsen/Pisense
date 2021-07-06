import requests

def postDB(type, encoded_token):
    res = requests.post("https://pisense-server.herokuapp.com/{0}/{1}".format(type ,encoded_token))
    return res.status_code