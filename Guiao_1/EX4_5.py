import math
f=lambda x,y: x+y
g=lambda x,y: x*y
h=lambda x,y: x-y

#Para uma funçao produzir outra funçao tem que ser atraves de uma exp lambda
def special(f,g,h):
    return lambda x,y,z: h(f(x,y),g(y,z))

result=special(f,g,h)
 
    
print("Resultado da funçao special com argumentos 1,2,3: %d"%(result(1,2,3)))