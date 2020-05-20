import numpy as np
import math
from flappygame import play
import random

base = [-0.252165132632152, -0.125465654654654165, -0.62625521521526,-0.365545284852,-0.4054554656265656,1.982126516512]
#base = [0,0,0,0,0,0]
class NeuralNet():
    
    def __init__(self, W1=None, W2=None):
        self.InpNodes = 2
        self.HiddenNodes = 2
        self.OutNodes = 1
        if W1 and W2:
            self.W1 = W1
            self.W2 = W2
        else:
            self.random()

    def random(self):
        weightslist = []
        for weight in base:
            weightslist.append(weight + random.triangular(weight - .3, weight + .3))
        self.listtonet(weightslist)

    def listtonet(self, weightslist):
        W1 = []
        W2 = []
        count = 0
        for i in xrange(self.InpNodes):
            n = [] 
            for j in xrange(self.HiddenNodes):
                n.append(weightslist[count])
                count += 1
            W1.append(n)
        for i in xrange(self.HiddenNodes):
            n = [] 
            for j in xrange(self.OutNodes):
                n.append(weightslist[count])
                count += 1
            W2.append(n)
        self.W1 = W1
        self.W2 = W2

    def forward(self, inputvalues):
        hiddenlayeroutput = self.sigmoid(np.dot(inputvalues, self.W1))
        output = self.sigmoid(np.dot(hiddenlayeroutput, self.W2))
        return output

    def nettolist(self):
	weightslist = []
        for i in self.W1:
            weightslist.extend(i)
	for i in self.W2:
            weightslist.extend(i)
        return weightslist


    def sigmoid(self, n):
        return 1/(1 + np.exp(-n))
