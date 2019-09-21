



def concatenate(list_a,list_b):
    if list_a==[]:
        return list_b
    c=concatenate(list_a[1:],list_b)
    c[:0]=[list_a[0]]
    return c


    
list =[1,2,3]
list_y =[1,2,4,4]

print(concatenate(list,list_y))