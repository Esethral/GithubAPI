import requests
import json

def getRequest(user):
    URL = "https://api.github.com/users/"+user+"/repos"
    r = requests.get(url = URL)
    return r.json()

print(getRequest("esethral"))