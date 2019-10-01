

def getLen(list):
    if list==[]:
        return 0
    else:
        return 1+ getLen(list[1:])
    
list =[1,2,3]
print(getLen(list))