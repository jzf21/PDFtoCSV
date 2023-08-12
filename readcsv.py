import csv
f = open("test.csv", "r")
r = csv.reader(f)
for i in r:
    print(i)
