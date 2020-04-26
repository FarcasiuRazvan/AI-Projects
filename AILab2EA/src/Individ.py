'''
Created on Mar 27, 2019

@author: Wolf
'''
from random import random, randint
from copy import deepcopy

class individ(object):
    '''
    classdocs
    '''


    def __init__(self, lista,length,table,t):
        '''
        Constructor
        '''
        self.__lista=lista #the list of notified members
        self.Fitness=0
        self.__length=length #the number of notified members
        self.__table=table
        self.__t=t
        self.__vizitati=lista
        self.fitness(table,t)
    
    '''
    Keeps the number of the notified members and in the place of one member notify another
    '''
    def mutate(self,pm):
        if pm>random():
            ok=0
            while True:
                p=randint(0,len(self.__lista)-1)
                if self.__lista[p]==0 and ok==1:
                    self.__lista[p]=1
                    break
                if self.__lista[p]==1 and ok==0:
                    ok=1
                    self.__lista[p]=0
            
            self.fitness(self.__table, self.__t)
        return self
    
    '''
    Makes another individ that notifies the members from individ1 and individ2.
    self is inidivid1
    '''
    def crossover(self,individ2):
        lista=[]
        length=0
        
        for i in range(0,len(self.__lista)):
            lista.append(0)
        
        for i in range(0,len(self.__lista)):
            if self.__lista[i]==1 or individ2.getList()[i]==1:
                length+=1
                lista[i]=1
        return individ(lista,length,self.__table,self.__t)
    
    
    def bfs(self,coada,table,t):
        
        if t==0:
            return 0
        t-=1
        for i in range(0,len(self.__lista)):
            if table[coada][i]==1 and self.__vizitati[i]==0:
                self.__vizitati[i]=1
                self.bfs(i,table,t)
        
    def setVizitati(self):
        self.__vizitati=deepcopy(self.__lista)
        
    
    def fitness(self,table,t):
        self.setVizitati()
        for i in range(0,len(self.__lista)):
            if self.__lista[i]==1:
                self.bfs(i,table,t)
        cont=0
        for i in range(0,len(self.__vizitati)):
            if self.__vizitati[i]==1:
                cont+=1
        self.Fitness=cont
        return cont
        
    def getList(self):
        return self.__lista
    
    def getLength(self):
        return self.__length