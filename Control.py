import numpy as np
import math
import Genetic
import NeuralNets as NN

CR = .9
MR = .05
generations = 50
netsize = 20

genome=[]
for i in range (0,netsize): 
    netelement = NN.NeuralNet()
    genome.append(netelement)

for i in range(0,generations):
    print 'GENERATION ' + str(i)
    genome = newnetlist(genome)
    #genome = sorted(genome, key=performance,reverse=True)
    play(False, genome[0])