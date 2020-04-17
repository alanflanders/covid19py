import pandas as pd
import sys
import getopt

THRESHOLD = 400
LEADCOLUMNS = 4
SKIPDATES = 0
MOVINGAVERAGEDAYS = 3 # days over which the daily cases are averaged
HELP = "program.py -i <inputfile> -o <outputfile> -c <lead columns> -t <threshold> -s <skip dates>"

inputfile = ''
outputfile = ''
print(sys.argv)

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:c:t:s:")
except getopt.GetoptError:
    print(HELP)
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print(HELP)
        sys.exit()
    elif opt in ("-i"):
        inputfile = arg
    elif opt in ("-o"):
        outputfile = arg
    elif opt in ("-c"):
        LEADCOLUMNS = int(arg)
    elif opt in ("-t"):
        THRESHOLD = int(arg)
    elif opt in ("-s"):
        SKIPDATES = int(arg)


df = pd.read_csv(inputfile)

print(df.iloc[0:6,0:6])


dates = list(df)[LEADCOLUMNS+SKIPDATES:]

# Define the transformation
dict_transform = {}
for column in list(df)[0:LEADCOLUMNS]:
    dict_transform[column] = []
dict_transform["Cases Pct Changed"] = []
dict_transform["Date"] = []
dict_transform["Cases"] = []
dict_transform["Total Cases"] = []
dict_transform["Threshold Days"] = []
dict_transform["Cases MvAvg"] = []

for i, row in df.iterrows():
    print("Processing row: {}".format(i))
    dict_row = {}

    cases = 0
    totalcases = 0
    thresholddays = 0
    casequeue = []

    for i, date in enumerate(dates):
        # Copy first colunns
        for column in list(df)[0:LEADCOLUMNS]:
            dict_transform[column].append(row[column])

        casevalue = int(str(row[date]).replace(',','').split('.')[0])

        if cases != 0 and totalcases > 100:
             dict_transform["Cases Pct Changed"].append(((casevalue - totalcases)-cases) / cases)
        else:
             dict_transform["Cases Pct Changed"].append(0)

        cases = casevalue - totalcases 
        totalcases = casevalue
        dict_transform["Cases"].append(cases)
        dict_transform["Total Cases"].append(casevalue)
        dict_transform["Date"].append(date)

        if casevalue > THRESHOLD:
            thresholddays += 1
            dict_transform["Threshold Days"].append(thresholddays)
        else:
            dict_transform["Threshold Days"].append(0)

        # Moving average of new cases
        casequeue.append(cases)
        if len(casequeue) > MOVINGAVERAGEDAYS:
            casequeue.pop(0)
        dict_transform["Cases MvAvg"].append(sum(casequeue)/len(casequeue))


df_trans = pd.DataFrame.from_dict(dict_transform)

print(df_trans.iloc[0:120,0:7])

df_trans.to_csv(outputfile)
