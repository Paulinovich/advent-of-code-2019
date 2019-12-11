def mDistanceClosestIntersection(file):
   circuits = getListsCircuits(file)
   dictionaryLocations = saveInDictionary(circuits)
   manhattanDistances=[]
   
   for i in dictionaryLocations:
       for j in dictionaryLocations[i]:
           if dictionaryLocations[i][j] > 1 and not (i==0 and j==0):
               manhattanDistances.append(manhattanDistance(i,j))
               return (list(filter(None, manhattanDistances))).sort()[0]
               #gets a NoneType error somewhere


def saveInDictionary(circuits):
    # positions ={horizontalIndex:{verticalIndex: amountWires}}
    positions = {0:{0:0}}
    for circuit in circuits:
        # start position set as current position 
        curHor = 0;
        curVert = 0;
        for move in circuit:
            direction = move[0]
            steps = int(move[1:])
            newVert = curVert
            newHor = curHor
            if direction == 'R':
                newHor += steps
            elif direction == 'L':
                newHor += steps
            elif direction == 'U':
                newVert += steps
            elif direction == 'D':
                newVert -= steps
                
            # iterate over possible horizontal moves: the outsides dictionary's keys
            for i in range(min(curHor, newHor), max(curHor, newHor)+1):
                # iterate over possible vertical moves: the inside dictionary's keys
                for j in range(min(curVert, newVert), max(curVert, newVert)+1):
                    if i in positions:
                        if j in positions[i]:
                            positions[i][j] += 1
                        else:
                            positions[i][j] = 1
                    else:
                        positions[i] = {j:1}
            # update current position        
            curHor = newHor
            curVert = newVert
    return positions

def manhattanDistance(i, j):
    return abs(i) + abs(j)
    


def getListsCircuits(file):
    fopen = open(file)
    lines = []
    circuits=[]
    for line in fopen:
        lines.append(line.rstrip())
    for line in lines:
        circuitSolo = []
        circuitSolo = line.split(",")
        circuits.append(circuitSolo)
    return circuits


print(mDistanceClosestIntersection('inputDay3.txt'))