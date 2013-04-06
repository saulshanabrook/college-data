import sys
import pandas as pd
import csv


def dialect_from_path(path):
    with open(path, 'rb') as path:
        return csv.Sniffer().sniff(path.read(1024 * 5))


def datafrom_from_csv(path):
    return pd.read_csv(path, index_col=0, dialect=dialect_from_path(path))

files = sys.argv[1:]
dataframes = map(datafrom_from_csv, files)
final_dataframe = dataframes[0].join(dataframes[1], how='outer')
final_dataframe.to_csv('Cleaned/final.csv')
