'''
Created on May 20, 2019

@author: Wolf
'''
from random import *
from numpy import *

def sigmoid(s):
    return 1/(1 + exp(-s))

def derivata(s):
    return s * (1 - s)