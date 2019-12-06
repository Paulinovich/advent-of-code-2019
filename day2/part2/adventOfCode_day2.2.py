def findVerbNoun(file):
    listProgram=[]
    fopen = open(file)
    for line in fopen:
        numbers = line.rstrip().split(",")
        for number in numbers:
            listProgram.append(int(number))
   
    for i in range(100):
        for j in range(100):
            copyLP = listProgram[:]
            copyLP[1]=i
            copyLP[2]=j
            if intcode(copyLP)==19690720:
                return 100*i+j

   
def intcode(listProgram):
    k=0
    l = len(listProgram)-3
    while k<l:
        posItem1 = listProgram[k+1]
        posItem2 = listProgram[k+2]
        where = listProgram[k+3]
        if listProgram[k]==1:
            result = listProgram[posItem1] + listProgram[posItem2]
            try:
                listProgram[where] = result
            except: 
                break
        elif listProgram[k]==2:
            result = listProgram[posItem1] * listProgram[posItem2]
            try:
                listProgram[where] = result
            except:
                break
        k+=4
    return listProgram[0]
    

print(findVerbNoun("inputDay2.txt"))