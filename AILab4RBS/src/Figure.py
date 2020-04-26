'''
Created on May 3, 2019

@author: Wolf
'''

class figure(object):
    '''
    classdocs
    '''


    def __init__(self, intervals, name, value):
        '''
        Constructor
        '''
        self.__intervals=intervals
        self.__name=name
        self.__value=value
    
    def getName(self):
        return self.__name
    def getIntervals(self):
        return self.__intervals
    def getValue(self):
        return self.__value
    def getMiu(self):
        miuSet=[]
        for i in self.__intervals:
            miuSet.append(i.getMiu(self.getValue()))
        return miuSet
        