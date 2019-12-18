'''
1. store input in list

2. save all different object (key) and orbits (values) in a dictionary.

3. while len(dict)!=1: 
    3.1. go over all dictionaries in the list and check if it's value is a key in one of the other dictionaries.
        3.1.1: yes: - make that value key in a new nested dictionary and append the orbitting dictionary as a value.
                    - pop that copied dictionary out of the list
        3.1.2: no: continue
    3.2. repeat the same process with the values of the nested dictionaries.
    3.3. and so on

4. iterate over the whole nested dictionary and count 'how deep' every value is and add this numbers together.
'''
import copy

def run(file):
    listInput = saveInput(file)
    dObj = dictObjects(listInput)
    # can we asume there is one starter object or could there be more? 
    #while len(lObj) != 1:
    # how to get 'deeper' with every call on the function? 
    dObj = restructure(dObj)
    return(dObj)


def saveInput(file):
    inp = []
    inputFile = open(file)
    for i in inputFile:
        inp.append(i.rstrip())
    return inp


def dictObjects(inp):
    dictObjects = {}
    for i in inp:
        split = i.index(')')
        key = i[:split]
        orbit = i[split+1:]
        if key not in dictObjects:
            dictObjects[key] = [orbit]
        else: 
            dictObjects[key].append(orbit)
    return dictObjects


def restructure(dObj):
    # keys in main dict dObj
    # making copy of dictionary because we can't iterate over objects that change size
    copyObj = copy.deepcopy(dObj)
    for i in dObj:
        # item in list of values of key
        for j in dObj[i]:
            if j in copyObj.keys(): 
                # add dictionary of orbit to list of values
                try: 
                    copyObj[i].append({j : copyObj[j]})
                # remove the duplicated value from list
                    copyObj[i].remove(j)
                # remove the copied key-value from the dictionary
                    del copyObj[j]
                except: 
                    pass
                
    return copyObj
                
                
                

print(run("input.txt"))