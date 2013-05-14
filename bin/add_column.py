from __future__ import print_function

import sys
import csv
import tempfile


tmp = tempfile.SpooledTemporaryFile()
_, souce_path, column, value = sys.argv
writer = csv.writer(tmp)
with open(souce_path, 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024 * 5))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect=dialect)
    line = 0
    for row in reader:
        line += 1
        if line == 1:
            new_row = [row[0], column]
        else:
            new_row = [row[0], value]
        writer.writerow(new_row)
    tmp.seek(0)
print(tmp.read(), end='')
