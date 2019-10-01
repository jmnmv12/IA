import math
f=lambda x,y: (math.sqrt(x**2+y**2),math.degrees(math.atan(y/x)))
 
    
print(f(-10,-5))