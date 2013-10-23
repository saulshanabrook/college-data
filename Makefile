convert_headers:
	python bin/convert_headers.py Raw\ Data/large.csv > Cleaned/Headers/large.csv

add_good_column:
	python bin/add_column.py Raw\ Data/good.csv 'To Visit' 1 > Cleaned/good_fixed.csv

add_change_lives_column:
	python bin/add_column.py Raw\ Data/change_lives.csv 'Change Lives' 1 > Cleaned/change_lives_fixed.csv

merge:
	python bin/merge.py Cleaned/Headers/large.csv Cleaned/small_fixed.csv Cleaned/good_fixed.csv Cleaned/change_lives_fixed.csv > Cleaned/final.csv

create_smaller:
	python bin/keep_columns.py Cleaned/final.csv > Cleaned/smaller_final.csv

all: convert_headers reorganize_small add_good_column merge create_smaller
