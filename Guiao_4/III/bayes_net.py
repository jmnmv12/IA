from itertools import product 

class BayesNet:

    def __init__(self, ldep=None):  # Why not ldep={}? See footnote 1.
        if not ldep:
            ldep = {}
        self.dependencies = ldep

    # Os dados estao num dicionario (var,dependencies)
    # em que as dependencias de cada variavel
    # estao num dicionario (mothers,prob);
    # "mothers" e' um frozenset de pares (mothervar,boolvalue)
    def add(self,var,mothers,prob):
        self.dependencies.setdefault(var,{})[frozenset(mothers)] = prob

    # Probabilidade conjunta de uma dada conjuncao 
    # de valores de todas as variaveis da rede
    def jointProb(self,conjunction):
        prob = 1.0
        for (var,val) in conjunction:
            for (mothers,p) in self.dependencies[var].items():
                if mothers.issubset(conjunction):
                    prob*=(p if val else 1-p)
        return prob

    def ancestors(self,var):
       

        all_frozen_set=[i for i in list(self.dependencies[var].keys())]
        all_ancestors=set()
        if(all_frozen_set==[frozenset()]):
            #print("hello")
            return []
        for i in all_frozen_set:
            for key in list(dict(i).keys()):
                all_ancestors.add(key)

        for ancestor in all_ancestors:
            all_ancestors=list(all_ancestors)
            all_ancestors+=self.ancestors(ancestor)
        return list(set(all_ancestors))
        

    def conjunction(self,listvars):

        all_conjunctions=list(product(listvars,[True,False]))
        print(f"List Vars: {all_conjunctions}")

        for j in all_conjunctions:
            for i in all_conjunctions:
                pass

        # TODO use zip





    def individual_prob(self,var):
        var_ancestors=self.ancestors(var)
        conjunctions=self.conjunction(var_ancestors)


# Footnote 1:
# Default arguments are evaluated on function definition,
# not on function evaluation.
# This creates surprising behaviour when the default argument is mutable.
# See:
# http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments

