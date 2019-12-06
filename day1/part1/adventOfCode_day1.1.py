import math

def fuelcalculator(file):
    neededFuel = 0
    
    fopen = open(file)
    for line in fopen:
        neededFuel += math.floor(int(line.rstrip())/3)-2
        
    return neededFuel
    
print(fuelcalculator('inputDay1.txt'))
    


