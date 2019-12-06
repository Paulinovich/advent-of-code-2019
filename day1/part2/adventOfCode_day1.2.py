import math

def totalfuelcalculator(file):
    neededFuel = 0
    fopen = open(file)
    for line in fopen:
        fuelToCalculate = fuelcalculator(int(line.rstrip()))
        neededFuel += fuelToCalculate
        iterate = True
        while iterate:
            fuelForFuel = fuelcalculator(fuelToCalculate)
            if fuelForFuel > 0:
                neededFuel += fuelForFuel
                fuelToCalculate = fuelForFuel
            else: iterate = False
                
    return neededFuel
    

def fuelcalculator(fuel):
    return math.floor(fuel/3)-2
    

print(totalfuelcalculator('inputDay1.txt'))
    




