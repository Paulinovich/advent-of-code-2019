def possibilities(x,y):
    pos=[]
    for i in range(x,y+1):
        digits=[int(j) for j in str(i)]
        if neverDecrease(digits)==True and sameAdjDigits(digits)==True:
            pos.append(i)
    return len(pos)

def neverDecrease(digits):
    for i in range(0, len(digits)-1): 
        if digits[i] > digits[i+1]:
            return False
    return True
    
def sameAdjDigits(digits):
    pairSeen = False
    for i in range(0, len(digits)-1): 
        if digits[i] == digits[i+1]:
            pairSeen = True
    return pairSeen

print(possibilities(197487, 673251))