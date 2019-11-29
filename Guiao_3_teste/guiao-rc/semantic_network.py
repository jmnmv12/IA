

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
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
#       self.relation = rel  # obsoleto
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

class AssocOne(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

class AssocNum(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,int(e2))

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

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

    def show_assoc(self):
        assoc=[d for d in self.declarations if  isinstance(d.relation,Association)]

        return assoc

    def show_members(self):
        members=[d.relation.entity1 for d in self.declarations if  isinstance(d.relation,Member)]

        return list(set(members))
    def show_users(self):
        members=[d.user for d in self.declarations ]

        return list(set(members))
    def show_types(self):
        members=[(d.relation.entity1,d.relation.entity2) for d in self.declarations if  isinstance(d.relation,Subtype)]
        members=[x for t in members  for x in t]
        return list(set(members))

    def local_assoc(self,e):
        assoc=[d.relation.name for d in self.declarations if  (d.relation.entity1==e or d.relation.entity2==e) and isinstance(d.relation,Association)]
        return list(set(assoc))

    def user_declared_rel(self,user):
        assoc=[d.relation.name for d in self.declarations if  d.user==user ]
        return list(set(assoc))

    def n_user_declared_rel(self,user):
        assoc=[d.relation.name for d in self.declarations if  d.user==user and isinstance(d.relation,Association)]
        
        return len(list(set(assoc)))
    
    def tuple_local_assoc(self,e):
        assoc=[(d.relation.name,d.user) for d in self.declarations if  (d.relation.entity1==e or d.relation.entity2==e) and isinstance(d.relation,Association)]
        return list(set(assoc))
    
    def predecessor(self,e1,e2):
        children=[d.relation.entity1 for d in self.declarations if d.relation.entity2==e1 and (isinstance(d.relation,Member) or isinstance(d.relation,Subtype))]

        for ch in children:
            if ch==e2:
                return True
            return self.predecessor(ch,e2)
        return False

    def predecessor_path (self,e1,e2):
        children=[d.relation.entity1 for d in self.declarations if d.relation.entity2==e1 and (isinstance(d.relation,Member) or isinstance(d.relation,Subtype))]

        for ch in children:
            if ch==e2:
                return [e1,e2]
            result=self.predecessor_path(ch,e2)
            if result!=None:
                return [e1] +result
        return None

    def query(self,e,first=True,assoc=None):
        if first:
            self.query_result=[i for i in self.query_local(e1=e,rel=assoc) if isinstance(i.relation,Association)]

        
        parent=[d.relation.entity2 for d in self.declarations if d.relation.entity1==e and (isinstance(d.relation,Member) or isinstance(d.relation,Subtype))]
        print
        for p in parent:
            self.query_result+=[i for i in self.query_local(e1=p,rel=assoc)+self.query(p,False,assoc) if isinstance(i.relation,Association)]
            self.query_result=list(set(self.query_result))
            
        return self.query_result

    def query2(self,e,first=True,assoc=None):
        if first:
            self.query_result=self.query_local(e1=e,rel=assoc)

        
        parent=[d.relation.entity2 for d in self.declarations if d.relation.entity1==e and (isinstance(d.relation,Member) or isinstance(d.relation,Subtype))]
        
        for p in parent:
            self.query_result+=self.query(p,True,assoc)
            self.query_result=list(set(self.query_result))
            
        return self.query_result
    def query_cancel(self,e,assoc):
        
        local_decl=[i for i in self.query_local(e1=e,rel=assoc) if isinstance(i.relation,Association)]
        parent=[d.relation.entity2 for d in self.declarations if d.relation.entity1==e and (isinstance(d.relation,Member) or isinstance(d.relation,Subtype))]
        
        for p in parent:
            my_result=[]
            my_result+=[i for i in self.query_local(e1=p,rel=assoc)+self.query_cancel(p,assoc) if isinstance(i.relation,Association)]
            my_result=list(set(my_result))
            temp_decl=[]
            for i in my_result:
                if i.relation.name not in [d.relation.name for d in local_decl ]:
                    temp_decl+=[i]
            local_decl+=temp_decl
        #print (local_decl)
        return local_decl
    def query_down(self,tipo,assoc,skip=True):
        children=[d.relation.entity1 for d in self.declarations if d.relation.entity2==tipo and (isinstance(d.relation,Member) or isinstance(d.relation,Subtype))]

        if skip:
            local_Decl=[]
        else:
            local_Decl=[d for d in self.declarations if d.relation.name==assoc and (isinstance(d.relation,Association) and d.relation.entity1==tipo)]

        for ch in children:
            
            local_Decl+=self.query_down(ch,assoc,False)

        return local_Decl
    
    def query_induce(self,tipo,assoc):
        decl=self.query_down(tipo,assoc)
        c=Counter([ n.relation.entity2 for n in decl])

        for elem in c.most_common(1):   
            return elem[0]
    
    def query_local_assoc(self,e,assoc):
        local_decl=self.query_local(e1=e,rel=assoc)
        
        if isinstance(local_decl[0].relation,AssocOne):
            total=len(local_decl)
            c=Counter([n.relation.entity2 for n in local_decl]).most_common()

            return c[0][1]/total
        if isinstance(local_decl[0].relation,AssocNum):
            total=len(local_decl)
            cumulative=0
            for elem in [d.relation.entity2 for d in local_decl]:
                cumulative+=elem
            return cumulative/total
        
        if isinstance(local_decl[0].relation,Association):
            total=len(local_decl)
            c=Counter([n.relation.entity2 for n in local_decl]).most_common()
            freqs=[ (elem[0],elem[1]/total) for elem in c]
            total_freq=0
            result=[]
            for elem in freqs:
                if total_freq>0.75:
                    return result
                total_freq+=elem[1]
                result.append(elem)

    def calc_predecessor_value(self,e,assoc,v):
        parent=[d.relation.entity2 for d in self.declarations if d.relation.entity1==e and (isinstance(d.relation,Member) or isinstance(d.relation,Subtype))]
        final_value=0
        for p in parent:
            local_decl=self.query_local(e1=p,rel=assoc)
            c=Counter( [n.relation.entity2 for n in local_decl]).most_common()
            if v in [elem[0] for elem in c]:
                n=[d[1] for d in c if d[0]==v]
                freq=n/len(local_decl)
                final_value=freq+self.calc_predecessor_value(p,assoc,v)
            else:
                final_value=0+self.calc_predecessor_value(p,assoc,v)
        return final_value

    def query_assoc_value(self,e,assoc):
        local_decl=self.query_local(e1=e,rel=assoc)

        c=Counter( [n.relation.entity2 for n in local_decl]).most_common()
        
        if len(c)==1:
            return c[0][0]

        parent=[d.relation.entity2 for d in self.declarations if d.relation.entity1==e and (isinstance(d.relation,Member) or isinstance(d.relation,Subtype))]
        if parent:
            freqs=[ (elem[0],elem[1]/len(local_decl)) for elem in c]
            f_total=[]
            for v in freqs:
                predecessor_value=self.calc_predecessor_value(e,assoc,v[0])
                final_value=(v[1]+predecessor_value)/2
                f_total.append((v[0],final_value))
            f_total.sort(key=lambda tup: tup[1],reverse=True)
            return f_total[0][0]
        else:
            freqs=[ (elem[0],elem[1]/len(local_decl)) for elem in c]
            if len(freqs)!=0:
                return freqs[0][0]





        
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
    

