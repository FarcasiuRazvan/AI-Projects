'''
Created on Apr 15, 2019

@author: Wolf
'''

class ant(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.solution=[]
    
    def fitness(self,problem):
        result=self.getResult(problem)
        
        sol=result+problem.get_column_words(result)
        
        return len([word for word in problem.words if word not in sol])
    
    def update(self,x):
        self.solution.append(x)
        
    def getResult(self,problem):
        result=[]
        for i in range(0,len(self.solution)):
            result.append(problem.words[self.solution[i]])
        return result
    
    def __str__(self):
        return str(self.solution)
    
    
    
    