import requests
import logging

logging.basicConfig(level=logging.INFO)

BASE = "http://127.0.0.1:5000/"
PATH = "putperson/"

response = requests.post(BASE + PATH + "401", json={
  "data": [
    {
      "id": "1",
      "personal": {
        "personalId": "XXX",
        "firstname": "Pranay1143",
        "lastname": "Gawde",
        "location": "IN",
        "username": "991pran3a21y"
      },
      "work": {
        "orgId": "XXXX",
        "orgName": "XXXX",
        "orgLocation": "XXX"
      }
    },
    {
      "id": "2",
      "personal": {
        "personalId": "XXX",
        "firstname": "Pranay1143",
        "lastname": "Gawde",
        "location": "IN",
        "username": "991pran3a21y"
      },
      "work": {
        "orgId": "XXXX",
        "orgName": "XXXX",
        "orgLocation": "XXX"
      }
    }
  ]
})
status_code = response.status_code
logging.info("Status code is %s", status_code)

if status_code == 200:
    logging.info("Valid JSON response")
    json_response = response.json()
    logging.info(json_response)
else:
    logging.info("Invalid response. HTTP code %s", status_code)
