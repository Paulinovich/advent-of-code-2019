def possibilities(x,y):
    pos=0
    for i in range(x,y+1):
        print(i)
        print(pos)
        if criteria(i)==True:
            pos+=1
    return pos


def criteria(number):
    digits=[int(j) for j in str(number)]
    pairs=True
    i=0
    while i<4:
        if digits[i] > digits[i+1]:
            print("out", number)
            return False
        elif digits[i] == digits[i+1]:
            pairs+=1
            # look for groups 
            if i<4:
                print(i)
                for j in range(2, (6-i)):
                    #blocks at 222223
                    print(j)
                    group=False
                    if digits[i] < digits[(i+j)]:
                        i+=j
                    if digits[i] > digits[(i+j)]:
                        return False
                    else: 
                        group=True
                # undo added pair from line 17
                if group==True:
                    pairs-=1
                    i+=j
        else:
            i+=1
            
    return pairs>0
                    


# result is too low
print(possibilities(197487, 673251))