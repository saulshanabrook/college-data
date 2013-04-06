convert_headers:
	python convert_headers.py Raw\ Data/small.csv > Cleaned/Headers/small.csv
	python convert_headers.py Raw\ Data/large.csv > Cleaned/Headers/large.csv

merge:
	python merge.py Cleaned/Headers/*

all: convert_headers merge
