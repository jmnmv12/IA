


def sub_set(list_a,):
    
    if(list_a==[]):
        
        return []
    list_new=[]
    list_new[:0]=[list_a] # adiciona a lista original
    list_new[:0]=[[list_a[0],i] for ind,i in enumerate(list_a) if ind!=0 and [list_a[0],i] not in list_new] 
    

    #list_b
    list_new[:0]=[[i] for i in list_a if i==list_a[0] and [i] not in list_new] #adiciona os elementos singulares
    list_new[:0]=sub_set(list_a[1:])

    #list_b=[i for i in list_new if len(i)==1]
    #list_new[:0]=list_b
         
    return list_new


    

   
    
    
    
list =[1,2,3]
list_b =[1,2,4,5]



print(sub_set(list_b))