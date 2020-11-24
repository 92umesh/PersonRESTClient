import csv
from get_by_id import *

with open('person_file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        # if line_count == 0:
        print(row)
        print(f'Column names are {", ".join(row)}')
        call_mock_rest(row["location"])
        # line_count += 1
        print(f'\t{row["location"]}')
        # line_count += 1
    # print(f'Processed {line_count} lines.')
