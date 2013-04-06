# What is this?

I am fed up with crappy "Find a College that works for you!" sites. They often take a lot of college data and simplify it down to a few toggles where you can
select how big you want the school to be and so on. I cut out the middleman and went straight to the sources [IPEDS](http://nces.ed.gov/ipeds/). The U.S.
Federal government requires that all U.S. colleges provide a ton of data every year. They release this data in nice little csv files. Well maybe not so nice.
Thats why I need this projet, to take CSV files exported by their ["Download Custom Data Files"](http://nces.ed.gov/ipeds/datacenter/InstitutionByName.aspx)
and merge the files it exports and to clean up the header rows to be more readable.

The exported files are in `Raw Data/`, I choose many variables to export, that would be applicable to me. All IPEDS schools are included in this data set.

# How do I make it wokr?

`make clean`

Takes `Raw Data/large.csv` and `Raw Data/small.csv` and merges them and fixes their column names. Exports it to `Cleaned/final.csv`

# But then what do I do?

I use [OpenRefine](http://openrefine.org/) to filter this data. [Google Fusion Tables](http://www.google.com/drive/start/apps.html#fusiontables)
is also nice for mapping the data and it works with Google Drive.
