
from constraintsearch import *
import itertools


def queen_constraint(r1,c1,r2,c2):
    l1 = int(r1[1:])
    print(f"L1: {l1} {r1}")
    l2 = int(r2[1:])
    if c1==c2:
        return False
    if abs(l1-l2)==abs(c1-c2):
        return False
    return True

def make_constraint_graph(n):
    queens = [ 'R'+str(i+1) for i in range(n) ]
    return { (X,Y):queen_constraint for X in queens for Y in queens if X!=Y }

def make_domains(n):
    queens = [ 'R'+str(i+1) for i in range(n) ]
    cols = [ i+1 for i in range(n) ]
    return { r:cols for r in queens }

cs = ConstraintSearch(make_domains(4),make_constraint_graph(4))

print(cs.search())

#Region colors exercise (Guiao TP - IV.4)

variables=['a','b','c','d','e']
values=['r','g','b'] #Partimos  com 3 cores e vamos aumentando ate chegar a uma solução e perceber qual o numero minimo de cores
domains={v:values for v in variables}
edges=[('a','b'),('b','c'),('c','d'),('d','a')] + [ (v,'e') for v in variables[:4] ]
edges =[ (v2,v1) for (v1,v2) in edges ] + edges # To obtain the inverted edges
graph= { e:(lambda v1,x1,v2,x2: x1!=x2) for e in edges} #For two conected edges we cant have the same color 

cs=ConstraintSearch(domains,graph)
print(cs.search())

#Friends exercise (Guiao TP - IV.5)

variables=['Andre','Bernardo','Claudio']
values_bike=['Bike Claudio','Bike Andre'] #Partimos  com 3 cores e vamos aumentando ate chegar a uma solução e perceber qual o numero minimo de cores
values_hat=['Hat Bernardo','Hat Andre'] #Partimos  com 3 cores e vamos aumentando ate chegar a uma solução e perceber qual o numero minimo de cores
possible_values=list(itertools.product(values_bike, values_hat))
values=[]
for v in possible_values:
    v1=v[0]
    v2=v[1]
    name1=v1.split()[1]
    name2=v2.split()[1]
    if name1!=name2 :
        values.append(v)
values.append(('Bike Bernardo','Hat Claudio'))    

domains={v:values for v in variables}
edges=[ (X,Y) for X in variables for Y in variables if X!=Y  ]
graph= { e:(lambda v1,x1,v2,x2: x1[0]!=x2[0] and x1[1]!=x2[1]) for e in edges} #For two conected edges we cant have the same color 

cs=ConstraintSearch(domains,graph)
print(cs.search())