'''
Created on May 20, 2019

@author: Wolf
'''

from random import *
from numpy import *
from Neuron import *

class Layer:
    '''
    classdocs
    '''
    def __init__(self, neuronNo, inputNo):
        '''
        Constructor
        '''
        self.neuronNo = neuronNo
        self.neurons = [Neuron(inputNo) for k in range(self.neuronNo)]
        
        
        
        
        
        
        