

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2018
# v1.81 - 2018/11/18
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#
from collections import Counter 

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')
class AssocOne(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

class AssocNum(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,float(e2))
# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=[]):
        self.declarations = ldecl
    def __str__(self):
        return my_list2string(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def show_all_association(self):
        result =set([ d.relation.name for d in self.declarations if isinstance(d.relation,Association)])
        return list(result)

    def show_all_members(self):
        result =set([ d.relation.entity1 for d in self.declarations if d.relation.name=='member'])
        return list(result)

    def show_all_users(self):
        result =set([ d.user for d in self.declarations])
        return list(result) 

    def show_all_types(self):
        result_a =([ d.relation.entity2 for d in self.declarations if d.relation.name=='member'])
        result_b =([ d.relation.entity1 for d in self.declarations if d.relation.name=='subtype'])
        result_c=([ d.relation.entity2 for d in self.declarations if d.relation.name=='subtype'])

        return list(set(result_b+result_a+result_c))

    def get_local_associations (self,e):
        result =set([ d.relation.name for d in self.declarations if isinstance(d.relation,Association) and (e==d.relation.entity2 or d.relation.entity1 == e)])
        return list(result) 

    def show_user_declarations(self,user):
        result =set([ d.relation.name for d in self.declarations if isinstance(d.relation,Association) and (d.user==user)])
        return list(result) 
    
    def count_user_declarations(self,user):
        result =set([ d.relation.name for d in self.declarations if isinstance(d.relation,Association) and (d.user==user)])
        return len(list(result))

    def user_association_declaration(self,e):
        result =set([ (d.relation.name,d.user) for d in self.declarations if isinstance(d.relation,Association) and (e==d.relation.entity2 or d.relation.entity1 == e)])
        return list(result) 

    def predecessor(self,e1,e2): #EX 2.9
        result=set([ d for d in self.declarations if (d.relation.name=='subtype' or d.relation.name=='member') and d.relation.entity2==e1])
        #print(f"Relation : {result}")
        if result==set():
            return False

        for entity in result:
            if(entity.relation.entity1==e2):
                return True    
                
            flag=self.predecessor(entity.relation.entity1,e2)
            
            if flag:
                return flag
        return False

    def predecessor_path(self,e1,e2): #EX 2.10
        result=set([ d for d in self.declarations if (d.relation.name=='subtype' or d.relation.name=='member') and d.relation.entity2==e1])
        path=[]
       
        #print(f"Relation : {result}")
        if result==set():
            return None
        
        for entity in result:
            if(entity.relation.entity1==e2):
                return [e1]+[entity.relation.entity1]
            #print(f"Relation: {e1}")
    
            flag=self.predecessor_path(entity.relation.entity1,e2)
            if flag:
                #print(f"Relation : {e1}")        
                return [e1]+flag
        
        return None

    def query(self,e1,relation=None):
        if relation is None:
            result=([ d for d in self.declarations if d.relation.entity1==e1 ])
            parents=set([ d for d in self.declarations if (d.relation.name=='subtype' or d.relation.name=='member') and d.relation.entity1==e1])
            #print(result)
            
                #pass
            #print(f"Result {result} Parents {parents}")
            #print(f"Parents: {result}")
            
            for p in parents:
                check=self.query(p.relation.entity2,None)
                #print(f"ResultV3 {check}")
                if check :
                    return result+check
            print("---")
            #print(f"Parents: {parents} result {check}")

    def query_down(self,entity,relation,skip=True):
        suc=[self.query_down(d.relation.entity1,relation,skip=False) for d in self.declarations if (isinstance(d.relation,Member) or isinstance(d.relation,Subtype)) and d.relation.entity2==entity]     
        
        if skip: #para ser em entidades descendentes do tipo passado temos que ultrapassar a primeira 
            l=[]
        else:
            l=self.query_local(e1=entity,rel=relation)
        return [item for sublist in suc for item in sublist]+l

    def query_induce(self,entity,relation):
        desc=self.query_down(entity,relation)
        c=Counter([d.relation.entity2 for d in desc])
        
        for m in c.most_common(1): #verificamos se o tuple existe e retornamos o valor mais comum
            return m[0] 
        #if it reaches the end without any tuples it returns None

    def query_local_assoc(self,entity,relation):
        local=self.query_local(e1=entity,rel=relation)

        if local==[]:
            return []    
        
        if isinstance(local[0].relation,AssocNum):
            return sum([d.relation.entity2 for d in local])/len(local)
        elif isinstance(local[0].relation,AssocOne):
            c=Counter([d.relation.entity2 for d in local])
            v,count=c.most_common(1)[0]
            return v,count/len(local)
        else:
            c=Counter([d.relation.entity2 for d in local])
            fsum=0
            l=[]
            for v,count in c.most_common():
                l.append((v,count/len(local)))
                fsum+=count/len(local)

                if fsum>0.75:
                    break
            return l
    
    def query_assoc_value(self,entity,relation):
        local=self.query_local(e1=entity,rel=relation)

        if local==[]:
            return []

        c=Counter([d.relation.entity2 for d in local])
        if len(c)==1:
            return local[0].relation.entity2
        else:
            c=Counter([d.relation.entity2 for d in local])
            for v,count in c.most_common():
                print(count/len(local))
                


        





    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))


# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ", " + str(list[i])
   return s + " ]"
    

