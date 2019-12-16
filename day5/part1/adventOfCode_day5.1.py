def intcode(file):
    programs = saveInput(file)



def saveInput(file):
    listProgram=[]
    fopen = open(file)
    for line in fopen:
        numbers = line.rstrip().split(",")
        for number in numbers:
            listProgram.append(number)
    return listProgram
            

    

#give whole program as input to read all the values?
def readInstruction(listProgram):
    index = 0
    instruction = listProgram[index]
    opcode = instruction[-2 : ]
    parMode = instruction[:-2]
    # find next instruction: jump amount parameters?
    block = listProgram[index : (index + len(parMode))]
    parameters = findParameters(listProgram, block, parMode)
    
    
    
    readOpcode(opcode)
    
    
    instruction = listProgramm(index + len(parMode))
  
    
    
def findParameters(listProgram, block, parMode):
    parameters = []
    for i in range(-1, (-1-len(parMode)), -1):
        # look at parametermode and save value of parameter.
        if parMode[i] == "0":
            # position mode - get value at location
            parameters.append(listProgram[block[-i]])
        elif parMode[i] == "1":
            # immediate mode - get value
            parameters.append(block[-i])
        else:
            print("Something went wrong")
    return parameters
    

def readOpcode(x):
    if x == "01":
        # add
    elif x == "02":
        # multiply
    elif x == "03": 
        # save input
    elif x == "04":
        # give output
    



