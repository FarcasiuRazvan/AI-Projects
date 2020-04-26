'''
Created on May 3, 2019

@author: Wolf
'''
import sys
class interval(object):
    '''
    classdocs
    '''


    def __init__(self, params, name):
        '''
        Constructor
        '''
        self.__params=params
        self.__type=""
        self.__name=name
        self.setType()
        
    
    def getParams(self):
        return self.__params
    def getType(self):
        return self.__type
    def getName(self):
        return self.__name
    def setType(self):
        if len(self.__params)==3:
            self.__type="triangle"
        else:
            self.__type="trapezoid"
    
    def getMiu(self,x):
        if self.getType()=="triangle":
            divValue1=self.__params[1]-self.__params[0]
            if divValue1==0:
                a=sys.float_info.max
            else:
                a=(x-self.__params[0])/divValue1
            divValue2=self.__params[2]-self.__params[1]
            if divValue2==0:
                b=sys.float_info.max
            else:
                b=(self.__params[2]-x)/divValue2
            return max(0,min(a,1,b))
        else:
            divValue1=self.__params[1]-self.__params[0]
            if divValue1==0:
                a=sys.float_info.max
            else:
                a=(x-self.__params[0])/divValue1
            divValue2=self.__params[3]-self.__params[2]
            if divValue2==0:
                b=sys.float_info.max
            else:
                b=(self.__params[3]-x)/divValue2
            return max(0,min(a,1,b))