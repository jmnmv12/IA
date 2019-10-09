
# Modulo: tree_search
# 
# Fornece um conjunto de classes para suporte a resolucao de 
# problemas por pesquisa em arvore:
#    SearchDomain  - dominios de problemas
#    SearchProblem - problemas concretos a resolver 
#    SearchNode    - nos da arvore de pesquisa
#    SearchTree    - arvore de pesquisa, com metodos para 
#                    a respectiva construcao
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2018,
#  Inteligência Artificial, 2014-2018

from abc import ABC, abstractmethod

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal_state):
        pass

# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return state == self.goal

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent,cost,heuristic_cost): 
        self.state = state
        self.parent = parent
        if(parent==None):
            self.depth=0
            self.cumulative_cost=cost
            self.A_star_cost=cost+heuristic_cost

        else:
            self.depth=self.parent.depth+1
            self.cumulative_cost=parent.cumulative_cost+cost
            self.A_star_cost=parent.cumulative_cost+cost+heuristic_cost

        self.heuristic_cost=heuristic_cost
        

    def __str__(self):
        return "no(" + str(self.state) +","+str(self.depth)+ "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth',limit=0): 
        self.problem = problem
        root = SearchNode(problem.initial, None,0,problem.domain.heuristic(problem.initial,problem.goal))
        self.open_nodes = [root]# 
        self.strategy = strategy
        self.limit=limit
        #self.visited=set()
        self.solution_length=0
        self.n_terminal_nodes=0
        self.n_nonterminal_nodes=0
        self.medium_ramification=0
        self.solution_cost=0
        self.cumulative_depth=0
        self.average_depth=0
        self.higher_cumulative_cost_node=[root]
        

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        

        path = self.get_path(node.parent)
        path += [node.state]
        #self.solution_length=node.depth
        return(path)

    # procurar a solucao
    def search(self):
        while self.open_nodes != []:
            node = self.open_nodes.pop(0) #retira no a frente da fila
            if self.problem.goal_test(node.state):#verifica se satiafaz objetivo
                self.solution_length=node.depth
                self.solution_cost=node.cumulative_cost
                #print(self.higher_cumulative_cost_node[0].cumulative_cost)
                
                self.average_depth=self.cumulative_depth/(self.n_nonterminal_nodes+self.n_terminal_nodes)
                #print(self.average_depth)
                
                #print(self.solution_length)
                #print(self.n_terminal_nodes)
                #print(self.n_nonterminal_nodes)
                self.medium_ramification=((self.n_nonterminal_nodes+self.n_terminal_nodes)-1)/self.n_nonterminal_nodes
                #print(self.medium_ramification)
                return self.get_path(node)
            
            if any( n.cumulative_cost<node.cumulative_cost for n in self.higher_cumulative_cost_node):
                self.higher_cumulative_cost_node=[]
                self.higher_cumulative_cost_node.append(node)
            elif any( n.cumulative_cost==node.cumulative_cost for n in self.higher_cumulative_cost_node):
                self.higher_cumulative_cost_node.append(node)

            if(self.strategy=='depth' and self.limit is not None and node.depth>self.limit): # A verificaçao tem de ser feita antes de expandir o no porque os nos filhos podem ter soluçao mas podem nao ser bons para expandir
                continue
            lnewnodes = []#se nao cria a lista de filhos
            self.n_nonterminal_nodes+=1
            result=self.problem.domain.actions(node.state)
            self.n_terminal_nodes+=len(result)-1
            for a in result:
                newstate = self.problem.domain.result(node.state,a) #para cada ação cria um novo estado
                state_cost=self.problem.domain.cost(newstate,a)
                heuristic_cost=self.problem.domain.heuristic(newstate,self.problem.goal)

                my_node=SearchNode(newstate,node,state_cost,heuristic_cost)
                node_depth=my_node.depth
                
                self.cumulative_depth+=node_depth
                #print(self.get_path(node))
                if(newstate not in self.get_path(node)):                    
                    
                    lnewnodes += [my_node]
                        #self.visited.add(newstate)
            #print(lnewnodes)
            #print(self.visited)
            self.add_to_open(lnewnodes)
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            sorted_list=sorted(lnewnodes, key=lambda x: x.cumulative_cost)
            self.open_nodes=self.union(sorted_list,self.open_nodes)
            
        elif self.strategy == 'greedy':
            self.open_nodes[:0] = sorted(lnewnodes, key=lambda x: x.heuristic_cost)
        elif self.strategy == 'A_star':
            self.open_nodes[:0] = sorted(lnewnodes, key=lambda x: x.A_star_cost )

    def concatenate(self,list_a,list_b):
        if list_a==[]:
            return list_b
        c=self.concatenate(list_a[1:],list_b)
        c[:0]=[list_a[0]]
        return c


    def union(self,list_a,list_b):
        

        list_new=[]
        if(list_a==[] and list_b==[]):
            return list_new
        elif list_a==[] and list_b!=[]:
            return list_new + list_b
        elif list_b==[] and list_a!=[]:
            return list_new + list_a
        else:
            if list_a[0].cumulative_cost<list_b[0].cumulative_cost:
                list_new.append(list_a[0])
                list_new=self.concatenate(list_new,self.union(list_a[1:],list_b))
            elif list_b[0].cumulative_cost<=list_a[0].cumulative_cost:
                list_new.append(list_b[0])
                list_new=self.concatenate(list_new,self.union(list_a,list_b[1:]))
            
        return list_new       


