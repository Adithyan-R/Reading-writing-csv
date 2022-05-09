# Importing csv module
import csv

#  Writing in CSV files

with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile) 
    writer.writerow(["Col 1", "Col 2"])
    writer.writerow( ["Data 1", "Data 2"])

#  Reading the CSV File

with open("data.csv", "r") as csvfile:
    reader= csv.reader(csvfile) 
    for row in reader:
        print(row)

# Appending in CSV File

with open ("data.csv", "a") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow( ["Data 3", "Data 4"])
     
  
with open ("data.csv", "r") as csvfile:
    reader= csv.DictReader (csvfile)
    for row in reader:
        print(row)


with open("data.csv", "w") as csvfile:
    fieldnames= ["id", "title"]
    writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id": 123, "title": "title 1"})
    writer.writerow({"id": 243, "title": "title 2"})
    writer.writerow({"id": 476, "title": "title 3"})



