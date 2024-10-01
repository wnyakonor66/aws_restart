import csv
import copy

myVehicle = {
    
    "vin" : "",
    "make" : "" ,
    "model" : "" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimeter = ',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'colu')