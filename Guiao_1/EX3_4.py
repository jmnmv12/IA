


def smallest_elem(list_a):
    
    if (list_a==[] ):
        
        return None
    min=list_a[0]

    min_candidate=smallest_elem(list_a[1:])
    
    if(min_candidate!=None):
        if min_candidate<min:
            
            min=min_candidate
            
    
    return min   
    
    


    

   
    
    
    
list_a =[2,1,4,34]




print(smallest_elem(list_a))