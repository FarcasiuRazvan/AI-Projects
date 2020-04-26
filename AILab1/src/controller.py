'''
Created on Mar 10, 2019

@author: Wolf
'''
from queue import Queue
from problem import Problem
from state import State
from copy import deepcopy
from _overlapped import NULL
from tkinter.constants import CURRENT

class Controller:

    def __init__(self, problem):
        self.__problem = problem
        self.__queque=Queue() #this will be the queue in which we will keep the still valid states
    
    def BFS(self):
        if self.__problem.heuristic():
            self.__queque.put(self.__problem.getInitial())
        else:
            return False
        
        while not self.__queque.empty():
            probleme=Problem(self.__queque.get())
            while True:
                #if probleme.heuristic():
                if probleme.isLeaf() and probleme.isValid():
                    return probleme.getCurrent()
                elif probleme.isLeaf()==False:
                    newproblem = State()
                    newproblem.setValues(deepcopy(probleme.getCurrent().getValues()))
                    #print(newproblem.getFrecv())
                    self.__queque.put(newproblem)
                if probleme.expand()==False:
                    break
        
        
            
        
        
        
        
        
        
        
    def Gbfs(self):
        if self.__problem.heuristic():
            self.__queque.put(self.__problem.getInitial())
        else:
            return False
        
        while not self.__queque.empty():
            probleme=Problem(self.__queque.get())
            while True:
                if probleme.isLeaf() and probleme.isValid():
                    return probleme.getCurrent()
                
                p=probleme.heuristic()
                if p:
                    newproblem = State()
                    newproblem.setValues(deepcopy(p.getValues()))
                    #print(newproblem.getFrecv())
                    self.__queque.put(newproblem)
                if probleme.expand()==False:
                    break
        