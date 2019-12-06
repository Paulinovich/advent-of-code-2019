def intcode(file):
    listProgram=[]
    fopen = open(file)
    for line in fopen:
        numbers = line.rstrip().split(",")
        for number in numbers:
            listProgram.append(int(number))
    # restore gravity assist program
    print(listProgram,"\n")
    listProgram[1]=12
    listProgram[2]=2
    print(listProgram,"\n")
    l = len(listProgram)-3
    i=0
    while i<l:
        item1 = listProgram[i+1]
        item2 = listProgram[i+2]
        if i==1:
            result = item1 + item2
            listProgram[i+3] = result
        elif i==2:
            result = item1 * item2
            listProgram[i+3] = result
        else:
            print("something went wrong")
        i+=4
    
    return listProgram
    
print(intcode("inputDay2.txt"))