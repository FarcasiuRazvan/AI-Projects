'''
Created on Mar 27, 2019

@author: Wolf
'''

class population(object):
    '''
    classdocs
    '''


    def __init__(self, length, v):
        '''
        Constructor
        '''
        self.__length=length
        self.__pop=v
    
    def getPopulation(self):
        return self.__pop
    def getLength(self):
        return self.__length
    def validate(self,lungime):
        i=0
        while i<len(self.__pop):
            if self.__pop[i].Fitness!=lungime:
                self.__pop.pop(i)
                self.__length-=1
                i-=1
            i+=1
        