from __future__ import print_function

from collections import defaultdict
import sys
import csv
import tempfile


def divide_values(dictionary, numerator, denominator):
    numerator = dictionary[numerator]
    denominator = dictionary[denominator]
    answer = float(numerator) / float(denominator)
    return round(answer, 2)

csv_path = sys.argv[1]
college_dict = defaultdict(lambda: {})
# Dict keys:
# ['award level code', 'cip code -  2010 classification', 'institution name', 'first or second major', 'grand total', 'cipcode', 'id of institution where data are reported for the completions component', 'unitid']
with open(csv_path, 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile, dialect=dialect)
    for row in reader:
        college = college_dict[row['unitid']]
        college['unitid'] = row['unitid']
        major_name = 'graduates ' + row['cip code -  2010 classification']
        college[major_name] = row['grand total']
        if 'graduates Grand total' in college:
            if 'graduates Computer Science' in college:
                college['percent graduates Computer Science'] = divide_values(college, 'graduates Computer Science', 'graduates Grand total')
            if 'graduates Computer Programming' in college:
                college['percent graduates Computer Programming'] = divide_values(college, 'graduates Computer Programming', 'graduates Grand total')


tmp = tempfile.SpooledTemporaryFile()

fieldnames = (
    'unitid',
    'graduates Grand total',
    'graduates Computer Science',
    'graduates Computer Programming',
    'percent graduates Computer Science',
    'percent graduates Computer Programming'
)
writer = csv.DictWriter(tmp, fieldnames=fieldnames)
headers = dict((n, n) for n in fieldnames)
writer.writerow(headers)
writer.writerows(college_dict.values())
tmp.seek(0)
print(tmp.read(), end='')
