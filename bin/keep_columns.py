from __future__ import print_function

import sys
import csv
import tempfile


tmp = tempfile.SpooledTemporaryFile()
_, source_path = sys.argv
columns_to_keep = [
    'instnm',
    'Control of institution',
    'Undergraduate offering',
    'Carnegie Classification 2010: Undergraduate Instructional Program',
    'Carnegie Classification 2010: Basic',
    "Carnegie Classification 2010: Undergraduate Profile",
    "Carnegie Classification 2010: Enrollment Profile",
    "Carnegie Classification 2010: Size and Setting",
    "Longitude location of institution",
    "Latitude location of institution",
    'Average net price (income 75-001-110-000)-students receiving Title IV Federal financial aid-2010-11',
    'Average net price (income over 110-000)-students receiving Title IV Federal financial aid- 2010-11',
    'percent graduates Computer and Information Sciences and Support Services',
    'To Visit'
]
with open(source_path, 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024 * 5))
    csvfile.seek(0)
    dict_reader = csv.DictReader(csvfile, dialect=dialect)
    dict_writer = csv.DictWriter(tmp, fieldnames=columns_to_keep)
    dict_writer.writer.writerow(columns_to_keep)
    for dict_row in dict_reader:
        for fieldname in dict_row.keys():
            if fieldname not in columns_to_keep:
                del dict_row[fieldname]
        dict_writer.writerow(dict_row)
    tmp.seek(0)
print(tmp.read(), end='')
