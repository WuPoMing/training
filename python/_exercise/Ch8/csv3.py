import csv

file = open('data2.csv', 'r')
fields = ["name","gender","score",
          "age","ageStage","birthday"]

csvCursor = csv.DictReader(file, fields)

for row in csvCursor:
    print(row['name'], row['score'])
    
file.close()
