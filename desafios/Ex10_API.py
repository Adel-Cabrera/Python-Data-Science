
import requests
import json

def request(url, method, payload=""):
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request(method, url, headers=headers,data = payload)

  if(method != 'DELETE'):
    return response.text #.encode('utf8')
  else:
    return response

