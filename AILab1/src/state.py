'''
Created on Mar 10, 2019

@author: Wolf
'''

class State:
    '''
    holds a node of the tree.
    '''
    def __init__(self):
        self.__values = []
        self.__frecvent=[]
    
    def setValues(self, values):
        self.__values = values[:]
        for i in range (0,len(self.__values)+1):
            self.__frecvent+=[0]
        
        for i in range (0,len(self.__values)):
            for j in range(0,len(self.__values[i])):
                self.__frecvent[self.__values[i][j]]+=1

    def getValues(self):
        return self.__values[:]
    def getFrecv(self):
        return self.__frecvent[:]
    def setFrecv(self,i,q):
        self.__frecvent[i]+=q
    def __str__(self):
        s=''
        for i in range (0,len(self.__values)):
            for j in range(0,len(self.__values[i])):
                s+=str(self.__values[i][j])+" "
            s+="\n"
        return s