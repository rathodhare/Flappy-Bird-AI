from flappygame import play
import random
from random import randint
import numpy as np
import math
import NeuralNets as NN

CR = .9
MR = .05
generations = 50
netsize = 20


def performance(n):
    return play(False,n)


def updateweights(n1, n2):
    a = random.random()
    WL1 = np.array(n1.nettolist())
    WL2 = np.array(n2.nettolist())
    C1 = WL1
    C2 = WL2
    if a < CR:
		WL1 = np.array(n1.nettolist())
		WL2 = np.array(n2.nettolist())
		C1 = [i * 0.5 for i in np.add(WL1, WL2)]
		C2 = [i * 0.5 for i in np.add(WL1, WL2)]

    b = random.random()
    c = random.random()
    if b < MR:
	    index = random.randint(0, len(C1) - 1)
	    C1[index] += random.triangular(-1, 1) * C1[index]
    if c < MR:
        index = random.randint(0, len(C2) - 1)
        C2[index] += random.triangular(-1, 1) * C2[index]

    n1.listtonet(C1)
    n2.listtonet(C2)
    return (n1, n2)

def survivaloffittest(genome):
    first = genome[random.randint(0, len(genome) - 1)]
    second = genome[random.randint(0, len(genome) - 1)]
    if performance(first) > performance(second):
        return first
    else:
        return second

def newnetlist(genome):
	newnetlist = []
	genome = sorted(genome, key=performance,reverse=True)
	newnetlist.extend(genome[0:5])

	while len(newnetlist) < len(genome):
		first = survivaloffittest(genome)
		second = survivaloffittest(genome)
		first, second = updateweights(first, second)
		newnetlist.append(first)
                newnetlist.append(second)
	return newnetlist

genome=[]
for i in range (0,netsize): 
    netelement = NN.NeuralNet()
    genome.append(netelement)

for i in range(0,generations):
    print 'GENERATION ' + str(i)
    genome = newnetlist(genome)
    #genome = sorted(genome, key=performance,reverse=True)
    play(False, genome[0])