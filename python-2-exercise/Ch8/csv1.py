import csv

file = open('data.csv', 'r')
csvCursor = csv.reader(file)

for row in csvCursor:
    print(row[0], row[2])
    
file.close()
