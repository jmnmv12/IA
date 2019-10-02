
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
    def __init__(self,state,parent): 
        self.state = state
        self.parent = parent
        if(parent==None):
            self.depth=0
        else:
            self.depth=self.parent.depth+1
    def __str__(self):
        return "no(" + str(self.state) +","+str(self.depth)+ "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth',limit=0): 
        self.problem = problem
        root = SearchNode(problem.initial, None)
        self.open_nodes = [root]# 
        self.strategy = strategy
        self.limit=limit
        #self.visited=set()
        self.solution_length=0
        self.n_terminal_nodes=0
        self.n_nonterminal_nodes=0
        self.medium_ramification=0

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
                #print(self.solution_length)
                #print(self.n_terminal_nodes)
                #print(self.n_nonterminal_nodes)
                self.medium_ramification=((self.n_nonterminal_nodes+self.n_terminal_nodes)-1)/self.n_nonterminal_nodes
                #print(self.medium_ramification)
                return self.get_path(node)
            lnewnodes = []#se nao cria a lista de filhos
            self.n_nonterminal_nodes+=1
            result=self.problem.domain.actions(node.state)
            self.n_terminal_nodes+=len(result)-1
            for a in result:
                newstate = self.problem.domain.result(node.state,a) #para cada ação cria um novo estado
                state_cost=self.problem.domain.cost(newstate,a)

                my_node=SearchNode(newstate,node)
                node_depth=my_node.depth
                #print(self.get_path(node))
                if(newstate not in self.get_path(node)):                    
                    if(self.limit>0):#se limite for >0 a pesquisa com limite esta ativada
                        if(node_depth<=self.limit):
                            lnewnodes += [my_node]
                            #self.visited.add(newstate)
                    else:
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
            pass

