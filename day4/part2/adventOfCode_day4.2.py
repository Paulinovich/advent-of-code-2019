def possibilities(x,y):
    pos=0
    for i in range(x,y+1):
        if criteria(i)==True:
            pos += 1
    return pos

def criteria(i):
    digits=[int(j) for j in str(i)]
    pairSeen=False
    numberPair=[]
    secondPairSeen=False
    groupSeen=False
    secondGroupSeen=False
    for i in range(0, len(digits)-1): 
        if digits[i] > digits[i+1]:
            return False
        elif digits[i] == digits[i+1]:
            if pairSeen == True and digits[i] not in numberPair:
                #mistake here: also true inside first group
                secondPairSeen = True
            if i<len(digits)-2 and digits[i] == digits[i+2]:
                if groupSeen==True:
                    secondGroupSeen=True
                groupSeen = True
            else: 
                pairSeen = True
                numberPair.append(digits[i])
    return result(pairSeen, secondPairSeen, groupSeen, secondGroupSeen)

def result(pair, secondPair, group, secondGroup):
    if pair==True:
        if secondPair==True and secondGroup == False:
            return True
        else:
            if group == False:
                return True
    return False


print(possibilities(197487, 673251))
# result is too low