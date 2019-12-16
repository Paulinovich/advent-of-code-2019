def mDistanceClosestIntersection(file):
    circuits = getListsCircuits(file)
    circuit1 = saveInDict(circuits[0])
    circuit2 = saveInDict(circuits[1])
    distances = []
    for i in circuit1:
        if i in circuit2:
            for j in circuit1[i]:
                if j in circuit2[i] and [i,j] != [0,0]: 
                    distances.append(manhattanDistance(i,j))
    distances.sort()
    return distances[0]
                
def saveInDict(circuit):
    # saving positions in dictionary with horizontal positions as key and a list of all vertical positions as value
    c={}
    # start position
    curHor = 0
    curVert = 0
    for move in circuit:
            direction = move[0]
            steps = int(move[1:])
            newHor = curHor
            newVert = curVert
            if direction == 'R':
                newHor += steps
            elif direction == 'L':
                newHor -= steps
            elif direction == 'U':
                newVert += steps
            elif direction == 'D':
                newVert -= steps
            for i in range(min(curHor, newHor), max(curHor, newHor)+1):
                 for j in range(min(curVert, newVert), max(curVert, newVert)+1):
                     if i in c:
                         c[i].append(j)
                     else: 
                         c[i]=[j]
            # update current position
            curHor = newHor
            curVert = newVert
    return c

def manhattanDistance(x,y):
    return abs(x) + abs(y)
    

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