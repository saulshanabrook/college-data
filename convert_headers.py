from __future__ import print_function

import sys
import csv
import tempfile


tmp = tempfile.SpooledTemporaryFile()
csv_path = sys.argv[1]
writer = csv.writer(tmp)
with open(csv_path, 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024 * 5))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    line = 0
    for row in reader:
        line += 1
        if line == 1:
            final_row = map(lambda header: header.split('-', 1)[-1], row)
        else:
            final_row = row
        writer.writerow(final_row)
    tmp.seek(0)
print(tmp.read(), end='')
