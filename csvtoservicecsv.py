from get_by_id import *
import logging

logging.basicConfig(level=logging.INFO)

"""
    this script calls call_mock_rest() in get_by_id.py which takes 'location' column from person_file.csv
    and fetches relevant data from PersonREST service
"""
with open('person_file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        logging.info(row)
        logging.info(f'Column names are {", ".join(row)}')
        call_mock_rest(row["location"])
        logging.info(f'\t{row["location"]}')
