from functools import reduce
f=lambda x,y: x*y




def reduce_apply(list_a,f):
    new=[reduce(f,i) for i in list_a]
    return new
    
    
    #final_list=[j for x in new for j in x]

    #return final_list


    #return list(map(lambda x: x+2,list_a))  
    
    
list_a=[[2,2],[5,1]]

 
    
print(reduce_apply(list_a,f))