'''
Created on May 3, 2019

@author: Wolf
'''

class repository(object):
    '''
    classdocs
    '''


    def __init__(self, figures):
        '''
        Constructor
        '''
        self.__figures=figures
    
    def getFigures(self):
        return self.__figures
    
        