# readcsv.py

import os
#print(os.listdir())

import csv

def ReadCSV():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file) # fr = file reader
        data = list(fr)
    #print(data)
    return data

alldata = ReadCSV()
#print(alldata)

for dt in alldata:
    print(dt[1])
