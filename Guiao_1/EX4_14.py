f=lambda x: x+2




def map_apply(list_a,f):
    new=[list(map(lambda x: x+2,i)) for i in list_a]
    final_list=[j for x in new for j in x]

    return final_list


    #return list(map(lambda x: x+2,list_a))  
    
    
list_a=[[2,2],[5,1]]

 
    
print(map_apply(list_a,f))