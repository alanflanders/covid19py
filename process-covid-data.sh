git -C /mnt/c/data/source/covid19/COVID-19 pull

python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv -o 02-changeovertime.csv -c 4

python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv -o 02-changeovertimedeaths.csv -c 4 -t 50

python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv -o 04-usdata.csv -c 11 -s 39

python3 01-dataframe-currentdata.py -i ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv -o 04-usdatadeaths.csv -c 12 -t 50 -s 39
