

def capicua(list_b):
        list_c=[i for ind,i in enumerate(list_b) if i==list_b[len(list_b)-(ind+1)]]
        if(len(list_c)==len(list_b)):
            return True
        else:
            return False

    
    
    
list =[1,2,1]


print(capicua(list))