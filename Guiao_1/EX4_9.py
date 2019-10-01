import math
f=lambda x,y: x>y


def special(list_a,f):
    
    if (list_a==[] ):
        
        return None
    min=list_a[0]

    min_candidate=special(list_a[1:],f)
    
    if(min_candidate!=None):
        if f(min_candidate,min):
            
            min=min_candidate
            
    
    return min   
list_a=[21,2,3]
 
    
print(special(list_a,f))