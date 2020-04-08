# Merge columns from multiple datasources
import pandas as pd
import sys
import getopt

LEADCOLUMNS = 4
TOCOLUMN = 4
HELP = "program.py -i <inputfile> -j <joinfile> -o <outputfile> -c <lead columns> -t <to column>"

inputfile = ''
outputfile = ''
colNames = []
print(sys.argv)

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:j:n:o:c:t:")
except getopt.GetoptError:
    print(HELP)
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print(HELP)
        sys.exit()
    elif opt in ("-i"):
        inputfile = arg
    elif opt in ("-j"):
        joinfile = arg
    elif opt in ("-n"):
        colNames = arg.split(",")
    elif opt in ("-o"):
        outputfile = arg
    elif opt in ("-c"):
        LEADCOLUMNS = int(arg)
    elif opt in ("-t"):
        TOCOLUMN = int(arg)


df = pd.read_csv(inputfile)

readCols = []
for i in range(LEADCOLUMNS, TOCOLUMN+1):
    readCols.append(i)

if len(colNames) > 0:
    dfj = pd.read_csv(joinfile, usecols=readCols, header=0, names=colNames)
else:
    dfj = pd.read_csv(joinfile, usecols=readCols)

df_trans = pd.concat([df, dfj], axis=1)
df_trans.drop([df_trans.columns[0]], axis='columns', inplace=True)

print(df_trans.iloc[0:120])

df_trans.to_csv(outputfile)
