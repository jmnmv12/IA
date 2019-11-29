
from bayes_net import *


bn = BayesNet()

bn.add('wol',[],0.6) #work overload
bn.add('uwp',[],0.05) #using word processor

#Acumulated unread email
bn.add('aue',[('wol',False )],0.001)
bn.add('aue',[('wol',True )],0.9) 

#Worried face
bn.add('wf',[('wol',True ),('nh',True )],0.02) 
bn.add('wf',[('wol',True ),('nh',False)],0.01)
bn.add('wf',[('wol',False),('nh',True )],0.011)
bn.add('wf',[('wol',False),('nh',False)],0.001)

#Needs help
bn.add('nh',[('uwp',True )],0.25) 
bn.add('nh',[('uwp',False)],0.004)

#High Mouse Frequency
bn.add('hmf',[('nh',True ),('uwp',True )],0.9) 
bn.add('hmf',[('nh',True ),('uwp',False)],0.1)
bn.add('hmf',[('nh',False),('uwp',True )],0.9)
bn.add('hmf',[('nh',False),('uwp',False)],0.01)

conjunction_true = [('wol',True),('uwp',True),('aue',True),('wf',True),('nh',True),('hmf',True)]
conjunction_false = [('wol',False),('uwp',False),('aue',False),('wf',False),('nh',False),('hmf',False)]


print(f"All True: {bn.jointProb(conjunction_true)}")
print(f"All False: {bn.jointProb(conjunction_false)}")
print(bn.individual_prob('hmf'))

