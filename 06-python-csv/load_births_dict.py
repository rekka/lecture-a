import csv

with open('US_births_2000-2014_SSA.csv') as f:
    data = list(csv.DictReader(f))

print(data[:10])
