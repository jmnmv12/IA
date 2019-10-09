def concatenate(list_a,list_b):
    if list_a==[]:
        return list_b
    c=concatenate(list_a[1:],list_b)
    c[:0]=[list_a[0]]
    return c


def union(list_a,list_b): #adapt to strategy
    

    list_new=[]
    if(list_a==[] and list_b==[]):
        return list_new
    elif list_a==[] and list_b!=[]:
        return list_new + list_b
    elif list_b==[] and list_a!=[]:
        return list_new + list_a
    else:
        if list_a[0]<list_b[0]:
            list_new.append(list_a[0])
            list_new=concatenate(list_new,union(list_a[1:],list_b))
        elif list_b[0]<=list_a[0]:
            list_new.append(list_b[0])
            list_new=concatenate(list_new,union(list_a,list_b[1:]))
         
    return list_new


    

   
    
    
    
list =[1,2,3]
list_b =[1,2,4,5]



print(union (list,list_b))