

def replace(list,a,b):
    list_c=[y if y!=a else b for y in list ]
    return list_c

    

   
    
    
    
list =[1,2,1]


print(replace (list,1,2))