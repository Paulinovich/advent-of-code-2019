"""
#1 search relations you and store the center and orbits
#2 for all these planets, do the same thing but don't go back to the one you came from
   +1 every step
#3 if this planet == san: return steps
   elif this planet doesn't have any centers or orbits: return None
   elif this planet = center: go deeper but not back to the one you came from
"""

def tranfersToSanta(file):
    inp = saveInput(file)
    borders, relations = infoPlanets(inp)
    
    #look for you and from there start looking for san
    return findrelations("YOU", None, relations, borders)
    
        
    
    
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
    ends = set()
    
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
    ends = planets.difference(centers)
    start = centers.difference(orbits)
    borders = ends.union(start)
    return borders, relations


def findrelations(planet, comingFrom, relations, borders):
    """
    (str) -> list
    
    saves all orbits and centers of a planet, except the one our recurstion is coming from.
    """
    transfers = []
    transfersPath = 0
    
    relations = []
    for i in relations:
        if planet in i:
            # both orbits and centers can be saved except itself and the one coming from
            for j in i: 
                if j not in (planet, comingFrom):
                    relations.append(j)
                    
    for rel in relations:
        if rel == "SAN":
            return transfers
        elif rel not in borders:
            transfers +=1
            transfers += findrelations(rel, comingFrom, relations, borders)
        
    transfers.append(transfersPath-1)
    return transfers
    
    
    
    

print(tranfersToSanta("input.txt"))