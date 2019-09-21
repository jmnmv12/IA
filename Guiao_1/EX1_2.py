

def getSum(list):
    if(len(list)==0):
        return 0

    else:
        return list[0]+getSum(list[1:])
    
    
list =[1,2,3]
print(getSum(list))