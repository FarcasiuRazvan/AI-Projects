'''
Created on May 20, 2019

@author: Wolf
'''
from random import *
from numpy import *

class Neuron(object):
    '''
    classdocs
    '''
    def __init__(self, inputNo):
        '''
        Constructor
        '''
        random.seed(1)
        self.inputNo = inputNo
        self.weights = [(random.random() * 2 - 1) for k in range(self.inputNo)]
        self.output = 0
        
    def setWeights(self,newWeights):
        self.weights=newWeights
        
        
        