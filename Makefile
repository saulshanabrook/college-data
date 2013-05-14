convert_headers:
	python bin/convert_headers.py Raw\ Data/small.csv > Cleaned/Headers/small.csv
	python bin/convert_headers.py Raw\ Data/large.csv > Cleaned/Headers/large.csv

reorganize_small:
	python bin/fix_cip.py Cleaned/Headers/small.csv > Cleaned/small_fixed.csv

add_good_column:
	python bin/add_column.py Raw\ Data/good.csv 'To Visit' 1 > Cleaned/good_fixed.csv

merge:
	python bin/merge.py Cleaned/Headers/large.csv Cleaned/small_fixed.csv Cleaned/good_fixed.csv Cleaned/final.csv

all: convert_headers reorganize_small add_good_column merge
