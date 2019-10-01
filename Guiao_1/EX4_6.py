import math
f=lambda x: -x>-20


#Para uma funçao produzir outra funçao tem que ser atraves de uma exp lambda
def special(list_a,h):
    new=[ i for i in list_a if h(i)==False]
    if new==[]:
        return True
    else:
        return False
list_a=[21,2,3]
 
    
print(special(list_a,f))