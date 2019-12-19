"""
New start after getting stuck with version using recursion on nested lists of dictionaries.
I cheated a bit and found inspiration in the solition of Musical_Muze (https://pastebin.com/u/Musical_Muze)
"""

def findSumOrbits(file):
    """
    (string) -> int
    
    saves all usefull information from the file and counts the total orbit sum.
    """
    inp = saveInput(file)
    orbits, relations = infoPlanets(inp)
    
    countAll = 0
    for orbit in orbits:
        countAll += countOrbits(orbit, relations)
    return countAll
    

def saveInput(file):
    """
    (String) -> list
    
    returns a list of all string items in a textfile
    """
    inp = []
    inputFile = open(file)
    for i in inputFile:
        inp.append(i.rstrip())
    return inp


def infoPlanets(inp):
    """
    (list) -> set, set, list of lists
    
    returns all unique orbits, all unique centers and all the orbit relations
    """
    planets = set()
    centers= set()
    orbits = set()
    relations = []
    
    for i in inp:
        split = i.index(')')
        center = i[:split]
        orbit = i[(split+1):]
        
        planets.add(center)
        planets.add(orbit)
        centers.add(center)
        orbits.add(orbit)
        relations.append([center, orbit])
        
    # remove the start center planet
    planets.remove(list(centers.difference(orbits))[0])
    return orbits, relations
    

def countOrbits(orbit, relations):
    """
    (string, list of lists) -> int
    
    count all occurences of a planet and it's orbits
    """
    count = 0
    for relation in relations:
        # planet has orbits
        if relation[0] == orbit:
            nextOrbit = relation[1]
            count += countOrbits(nextOrbit, relations)
        elif relation[1] == orbit:
            count += 1
    return count
    

print(findSumOrbits("input.txt"))