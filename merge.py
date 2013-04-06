import sys
import pandas as pd
import tempfile
import csv


def dialect_from_path(path):
    with open(path, 'rb') as path:
        return csv.Sniffer().sniff(path.read(1024 * 5))


def datafrom_from_csv(path):
    return pd.read_csv(path, index_col=0, dialect=dialect_from_path(path))

tmp = tempfile.SpooledTemporaryFile()
files = sys.argv[1:]
dataframes = map(datafrom_from_csv, files)
final_dataframe = dataframes[0].join(dataframes[1], how='outer')
print final_dataframe.ix[-20:, -3:].to_string()
tmp.seek(0)
print tmp.read()
