from __future__ import print_function

from collections import defaultdict
import sys
import csv
import tempfile


TOTAL_COLUMN = 'graduates Grand total'

csv_path = sys.argv[1]
college_dict = defaultdict(lambda: {})

fieldnames = []

with open(csv_path, 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile, dialect=dialect)
    for row in reader:
        college = college_dict[row['unitid']]
        college['unitid'] = row['unitid']
        major_name = 'graduates ' + row['cip code -  2010 classification']
        college[major_name] = row['grand total']
        fieldnames.append(major_name)

for college in college_dict.values():
    for key in college.keys():
        if key == 'unitid' or key == TOTAL_COLUMN:
            continue
        try:
            major_percent = round(
                float(college[key]) / float(college[TOTAL_COLUMN]),
                2
            )
        except (ZeroDivisionError, KeyError):
            pass
        else:
            major_percent_name = 'percent ' + key
            fieldnames.append(major_percent_name)
            college[major_percent_name] = major_percent

fieldnames = ['unitid'] + sorted(list(set(fieldnames)))
tmp = tempfile.SpooledTemporaryFile()
writer = csv.DictWriter(tmp, fieldnames=fieldnames)
headers = dict((n, n) for n in fieldnames)
writer.writerow(headers)
writer.writerows(college_dict.values())
tmp.seek(0)
print(tmp.read(), end='')
