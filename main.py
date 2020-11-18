import requests
import logging

logging.basicConfig(level=logging.INFO)

BASE = "http://127.0.0.1:5000/"
PATH = "/getJSON/"

response = requests.get(BASE + PATH + "2")
status_code = response.status_code
logging.info("Status code is %s", status_code)

if status_code == 200:
    logging.info("Valid JSON response")
    json_response = response.json()
    logging.info(json_response)
else:
    logging.info("Invalid response HTTP code %s", status_code)

