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
        posItem1 = listProgram[i+1]
        posItem2 = listProgram[i+2]
        where = listProgram[i+3]
        if listProgram[i]==1:
            result = listProgram[posItem1] + listProgram[posItem2]
            listProgram[where] = result
        elif listProgram[i]==2:
            result = listProgram[posItem1] * listProgram[posItem2]
            listProgram[where] = result
        i+=4
    
    return listProgram

print(intcode("inputDay2.txt")[0])