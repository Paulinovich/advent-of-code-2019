def possibilities(x,y):
    pos=0
    for i in range(x,y+1):
        if criteria(i)==True:
            print(i)
            pos+=1
    return pos


def criteria(number):
    digits=[int(j) for j in str(number)]
    pairs=0
    i=0
    while i<5:
        if digits[i] > digits[i+1]:
            return False
        # 2 seen
        elif digits[i] == digits[i+1]:
            pairs+=1
            if i<4:
                if digits[i] > digits[i+2]:
                    return False
                elif digits[i] == digits[i+2]:
                    #3 seen: troup: undo pair
                    pairs -= 1
                    if i<3:
                        if digits[i] > digits[i+3]:
                            return False
                        # 4 seen: still chance if i==0
                        elif digits[i] == digits[i+3]:
                            if i==0 and digits[i] < digits[i+4]:
                                i+=5
                            else:
                                return pairs>0
                        else:
                            i+=3
                    else: 
                        return pairs>0
                else: 
                    i+=2
            else: 
                return pairs>0
        else: i+=1
    return pairs>0
                
print(possibilities(197487, 673251))
#returns 1101, not correct