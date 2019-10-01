import math
f=lambda x,y: (math.sqrt(x**2+y**2),math.degrees(math.atan(y/x)))
 
    
def converter(x,y):
    return math.sqrt(x**2+y**2),math.degrees(math.atan(y/x))

def special(list_a):
    new=[converter(i,j) for (i,j) in list_a]
    return new
     
list_a=[(21,3),(20,2),(25,3)]
 
    
print(special(list_a))