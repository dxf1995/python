import csv
from os import read
'''

with open('nvme1n1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='', quotechar='|')
    for row in spamreader:
        print(', '.join(row))




with open('E:\python/day10/nvme1n1.csv', newline='', encoding='utf-8') as file_obj:
    reader = csv.reader(file_obj)
    for row in reader:
        print(reader)

'''
f = open('E:\python/day10/nvme1n1.csv', 'r')

with f:
    
    reader = csv.reader(f)

    for row in reader:
        for e in row:
            print(e)
            