def possibilities(x,y):
    pos=0
    for i in range(x,y+1):
        if criteria(i)==True:
            pos += 1
    return pos

def criteria(i):
    digits=[int(j) for j in str(i)]
    pairSeen=False
    for i in range(0, len(digits)-1): 
        if digits[i] > digits[i+1]:
            return False
        elif digits[i] == digits[i+1]:
            pairSeen = True
    return pairSeen

print(possibilities(197487, 673251))