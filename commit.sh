#!/bin/bash

rm 04-usdata.csv
rm 04-usdatadeaths.csv
git add .
git commit -m "$1"
git push
