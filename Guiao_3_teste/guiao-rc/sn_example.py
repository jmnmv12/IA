



# Redes semanticas
# -- Exemplo
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2019
# 2019/10/20
#


from semantic_network import *

a = Association('socrates','professor','filosofia')
s = Subtype('homem','mamifero')
m = Member('socrates','homem')

da = Declaration('descartes',a)
ds = Declaration('darwin',s)
dm = Declaration('descartes',m)

z = SemanticNetwork()
z.insert(da)
z.insert(ds)
z.insert(dm)
z.insert(Declaration('darwin',Association('mamifero','mamar','sim')))
z.insert(Declaration('darwin',Association('homem','gosta','carne')))

# novas declaracoes

z.insert(Declaration('darwin',Subtype('mamifero','vertebrado')))
z.insert(Declaration('descartes', Member('aristoteles','homem')))

b = Association('socrates','professor','matematica')
z.insert(Declaration('descartes',b))
z.insert(Declaration('simao',b))
z.insert(Declaration('simoes',b))

z.insert(Declaration('descartes', Member('platao','homem')))

e = Association('platao','professor','filosofia')
z.insert(Declaration('descartes',e))
z.insert(Declaration('simao',e))

z.insert(Declaration('descartes',Association('mamifero','altura',1.2)))
z.insert(Declaration('descartes',Association('homem','altura',1.75)))
z.insert(Declaration('simao',Association('homem','altura',1.85)))
z.insert(Declaration('darwin',Association('homem','altura',1.75)))

z.insert(Declaration('descartes', Association('socrates','peso',80)))
z.insert(Declaration('darwin', Association('socrates','peso',75)))
z.insert(Declaration('darwin', Association('platao','peso',75)))


z.insert(Declaration('damasio', Association('filosofo','gosta','filosofia')))
z.insert(Declaration('damasio', Member('socrates','filosofo')))


# Extra - descomentar as restantes declaracoes para o exercicio II.2.16

z.insert(Declaration('descartes', AssocNum('socrates','pulsacao',51)))
z.insert(Declaration('darwin', AssocNum('socrates','pulsacao',61)))
z.insert(Declaration('darwin', AssocNum('platao','pulsacao',65)))

z.insert(Declaration('descartes',AssocNum('homem','temperatura',36.8)))
z.insert(Declaration('simao',AssocNum('homem','temperatura',37.0)))
z.insert(Declaration('darwin',AssocNum('homem','temperatura',37.1)))
z.insert(Declaration('descartes',AssocNum('mamifero','temperatura',39.0)))

z.insert(Declaration('simao',Association('homem','gosta','carne')))
z.insert(Declaration('darwin',Association('homem','gosta','peixe')))
z.insert(Declaration('simao',Association('homem','gosta','peixe')))
z.insert(Declaration('simao',Association('homem','gosta','couves')))

z.insert(Declaration('damasio', AssocOne('socrates','pai','sofronisco')))
z.insert(Declaration('darwin', AssocOne('socrates','pai','pericles')))
z.insert(Declaration('descartes', AssocOne('socrates','pai','sofronisco')))
#print(z)
print("--EX 1--")
print(z.show_assoc())
print("--EX 2--")
print(z.show_members())
print("--EX 3--")
print(z.show_users())
print("--EX 4--")
print(z.show_types())
print("--EX 5--")
print(z.local_assoc('mamifero'))
print("--EX 6--")
print(z.user_declared_rel('descartes'))
print("--EX 7--")
print(z.n_user_declared_rel('descartes'))
print("--EX 8--")
print(z.tuple_local_assoc('mamifero'))
print("--EX 9--")
print(z.predecessor('vertebrado','socrates'))
print("--EX 10--")
print(z.predecessor_path('vertebrado','socrates'))
print("--EX 11 a)--")
z.query('socrates',True,'altura')
z.show_query_result()
print("--EX 11 b)--")
z.query2('socrates',True)
z.show_query_result()
print("--EX 12--")
print(z.query_cancel('socrates','altura'))
print("--EX 13--")
print(z.query_down('mamifero','altura'))
print("--EX 14--")
print(z.query_induce('mamifero','altura'))
print("--EX 15--")
print(z.query_local_assoc('socrates','pai'))
print("==========")
print(z.query_local_assoc('socrates','pulsacao'))
print("==========")
print(z.query_local_assoc('homem','gosta'))
print("--EX 16--")

print(z.query_assoc_value('homem','temperatura'))
