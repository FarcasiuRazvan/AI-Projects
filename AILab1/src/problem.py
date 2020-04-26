'''
Created on Mar 10, 2019

@author: Wolf
'''
from state import State
import math
from queue import Queue
from copy import deepcopy
from _overlapped import NULL

class Problem:
    
    def __init__(self, initial):
        self.__initialState = initial   #this will be the current root node
        self.__currentState = State()   #this will be the current node which we will verify
        self.__currentState.setValues(deepcopy(initial.getValues()))
        self.setCurrent()

    def expand(self):
        for i in range(0,len(self.__initialState.getValues())):
            for j in range(0,len(self.__initialState.getValues()[i])):
                if self.__initialState.getValues()[i][j]!=self.__currentState.getValues()[i][j] and self.__currentState.getValues()[i][j]<len(self.__initialState.getValues()[i]) :
                            self.__currentState.getValues()[i][j]+=1
                            self.__currentState.setFrecv(self.__currentState.getValues()[i][j],1)
                            self.__currentState.setFrecv(self.__currentState.getValues()[i][j]-1,-1)
                            return True
        return False
    def setCurrent(self):
        for i in range(0,len(self.__initialState.getValues())):
            for j in range(0,len(self.__initialState.getValues()[i])):
                if self.__currentState.getValues()[i][j]==0:
                            self.__currentState.getValues()[i][j]=1
                            self.__currentState.setFrecv(0,-1)
                            self.__currentState.setFrecv(1,1)
                            return True
        return False
    def getCurrent(self):
        return self.__currentState
            
    def getInitial(self):
        return self.__initialState
    def heuristic(self):
        ok=1
        qu=[]
        while True:
            for i in range(1,len(self.__currentState.getFrecv())):
                if self.__currentState.getFrecv()[i]>len(self.__initialState.getValues()):
                    ok=0
            if ok==1 :
                qu.append(self.__currentState)
            if self.expand()==False:
                break
        qu.sort(key=lambda x:(max(x.getFrecv())-min(x.getFrecv())))
        if(len(qu)):
            return qu[0]
        else:
            return NULL
    
    def isValid(self):
        
        for i in range(0,len(self.__currentState.getValues())):
            frec=[]
            for j in range (0,len(self.__currentState.getValues())+1):
                frec+=[0]
            for j in range(0,len(self.__currentState.getValues()[i])):
                frec[self.__currentState.getValues()[i][j]]+=1
            for j in range (1,len(self.__currentState.getValues())+1):
                if frec[j]>1:
                    return False
            
                    
        for i in range(0,len(self.__currentState.getValues())):
            frec=[]
            for j in range (0,len(self.__currentState.getValues())+1):
                frec+=[0]
            for j in range(0,len(self.__currentState.getValues()[i])):
                frec[self.__currentState.getValues()[j][i]]+=1
            for j in range (1,len(self.__currentState.getValues())+1):
                if frec[j]>1:
                    return False
    
        lengt=int(math.sqrt(len(self.__currentState.getValues())))
        for i in range(0,(len(self.__currentState.getValues())),lengt):
            for j in range(0,(len(self.__currentState.getValues())),lengt):
                for k in range(i,i+lengt):
                    frec=[]
                    for l in range (0,len(self.__currentState.getValues())+1):
                        frec+=[0]
                    for l in range(j,j+lengt):
                        frec[self.__currentState.getValues()[k][l]]+=1
                    for l in range (1,len(self.__currentState.getValues())+1):
                        if frec[j]>1:
                            return False
        
        
        return True
    
    def isLeaf(self):
        return self.__currentState.getFrecv()[0]==0
        
        
            
        