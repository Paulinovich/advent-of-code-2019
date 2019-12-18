def intcode(file):
    program = saveInput(file)
    run(program)


def saveInput(file):
    inputFile=open(file, "r")
    program = inputFile.read()
    inputFile.close()
    program  = program.split(",")
    return program
            

def run(program):
    index = 0
    #initial input = 1 (ID air conditioning unit)
    savedInput = 1
    
    while program[index] != "99":
        instruction, nextIndexStep = addParaModes(program[index])
        block = program[index : index + nextIndexStep]
        opcode = instruction[-2:]
        parMode = instruction[:-2]
        parameters = []
        # saving values of parameters of instruction in a lists, except where to store
        # parsing from right to left
        for i in range(-1, (-1-len(parMode)), -1):
            if parMode[i] == "0":
            # position mode - get value at location
                parameters.append(int(program[int(block[-i])]))
            elif parMode[i] == "1":
            # immediate mode - get value
                parameters.append(int(block[-i]))
            else:
                print("Something went wrong")
        # add last parameter as index: where to store:
        parameters.append(int(block[-1]))
    
        # read and execute the opcode
        program, savedInput = readOpcode(opcode, parameters, program, savedInput)
        if savedInput != None:
            print(savedInput)
        
        index += nextIndexStep
    return savedInput
  
def addParaModes(instruction):
    # third parameter is always 0 and not added. 
    if instruction[-1] in ["1", "2"]:
        instruction = (5-len(instruction)) * "0" + instruction
        nextIndexStep = 4
    elif instruction[-1] in ["3", "4"]:
        instruction = (3-len(instruction)) * "0" + instruction        
        nextIndexStep = 2
    return instruction, nextIndexStep


def readOpcode(opcode, parameters, program, inp):
    if opcode == "01":
        result = parameters[0] + parameters[1]
        program[parameters[-1]] = str(result)
    elif opcode == "02":
        result = parameters[0] * parameters[1]
        program[parameters[-1]] = str(result)
    elif opcode == "03": 
        program[parameters[-1]] = str(inp)
    elif opcode == "04":
        return program, str(parameters[0])
    return program, None
    

print(intcode("input.txt"))

