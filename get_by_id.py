import requests
import logging
from flask import json, jsonify
import yaml
import csv

logging.basicConfig(level=logging.INFO)


def write_csv(row):
    """
    this method creates header row and creates CSV file from
    :param row:
    :param fields:
    :return:
    """
    with open('GFG', 'w') as f:
        fields = ['username', 'id', 'firstname', 'lastname', 'location', 'mobile_number', 'work_id',
                  'org_id', 'org_location', 'org_name']
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(row)


def process_csv():
    """
    this method creates a row  for each element present in the json_list and adds it to the row array.
    :return:
    """
    row = []

    for each_element in json_list:
        logging.info(each_element)
        username = each_element[0]["username"]
        person_id = each_element[0]["id"]
        firstname = each_element[0]["firstname"]
        last_name = each_element[0]["lastname"]
        location = each_element[0]["location"]
        mobile_number = each_element[0]["mobile_number"]
        work_id = each_element[0]["work_id"]
        org_id = each_element[1]["org_id"]
        org_location = each_element[1]["org_location"]
        org_name = each_element[1]["org_name"]
        each_row = [username, person_id, firstname, last_name, location, mobile_number,
                    work_id, org_id, org_location, org_name]
        row.append(each_row)
    write_csv(row)


def call_mock_rest(person_id):
    logging.info('Processing started for ----- id' + str(person_id))
    global json_list
    base_path = "http://127.0.0.1:5000/"
    service_path = "getperson/"
    response = requests.get(base_path + service_path + str(person_id))
    status_code = response.status_code
    logging.info("Status code is %s", status_code)
    if status_code == 200:
        logging.info("Valid JSON response")

        json_response = response.json()
        list_dump = json.dumps(json_response)
        json_list = yaml.safe_load(list_dump)

        process_csv()


call_mock_rest(id)
