

def check(list,element):
    if(len(list)==0):
        
        return False
    elif(list[0]==element):
        return True

    else:
        return check(list[1:],element)
    
    
list =[1,2,3]
print(check(list,3))
