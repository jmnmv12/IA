


def equal_elem(list_a,list_b):
    new=[]
    if (list_a==[] and list_b==[]):
        return []
    elem=(list_a[0],list_b[0])
    new[:0]=[elem]
    
    new=new+equal_elem(list_a[1:],list_b[1:])
    return new
    


    

   
    
    
    
list_a =[2,5,6,7]
list_b =[2,3,5,5]



print(equal_elem(list_a,list_b))