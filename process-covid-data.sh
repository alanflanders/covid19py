# https://github.com/CSSEGISandData/COVID-19
git -C /mnt/c/data/source/covid19/COVID-19 pull

# Convert data shape
python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv -o 02-changeovertime.csv -c 4

python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv -o 02-changeovertimedeaths.csv -c 4 -t 50

# Not all locations reporting recoveries
#python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv -o 02-changeovertimerecovered.csv -c 4 -t 50

python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv -o 04-usdata.csv -c 11 -s 39

python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv -o 04-usdatadeaths.csv -c 12 -t 50 -s 39


# Merge columns
python3 05-dataframe-mergecols.py -i 02-changeovertime.csv -j 02-changeovertimedeaths.csv -o 05-mergedglobal.csv -c 7 -t 8 -n "Deaths,Total Deaths"
#python3 05-dataframe-mergecols.py -i 05-mergedglobal.csv -j 02-changeovertimerecovered.csv -o 05-mergedglobal.csv -c 7 -t 8 -n "Recoveries,Total Recoveries"

python3 05-dataframe-mergecols.py -i 04-usdata.csv -j 04-usdatadeaths.csv -o 05-mergedus.csv -c 15 -t 16 -n "Deaths,Total Deaths"


