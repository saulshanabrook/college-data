convert_headers:
	python convert_headers.py Raw\ Data/small.csv > Cleaned/Headers/small.csv
	python convert_headers.py Raw\ Data/large.csv > Cleaned/Headers/large.csv

reorganize_small:
	python fix_cip.py Cleaned/Headers/small.csv > Cleaned/small_fixed.csv

merge:
	python merge.py Cleaned/Headers/large.csv Cleaned/small_fixed.csv

all: convert_headers reorganize_small merge
