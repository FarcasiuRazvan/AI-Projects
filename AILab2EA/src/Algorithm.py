'''
Created on Mar 27, 2019

@author: Wolf
'''

from random import random,randint

class algorithm(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def iteration(self,table,pop,t,pM):
        i1=randint(0,pop.getLength()-1)
        i2=randint(0,pop.getLength()-1)
        
        if i1!=i2:
            c=pop.getPopulation()[i1].crossover(pop.getPopulation()[i2])
            c=c.mutate(pM)
            f1=pop.getPopulation()[i1].fitness(table,t)
            f2=pop.getPopulation()[i2].fitness(table,t)
            fc=c.fitness(table,t)
            if(f1>f2) and (f1>fc):
                pop.getPopulation()[i1]=c 
            if(f2>f1) and (f2>fc):
                pop.getPopulation()[i2]=c
        return pop
        
    def tests():
        minValues = [main()[0] for x in range(30)]
        print("Mean:", statistics.mean(minValues),
            "Stdev", statistics.stdev(minValues))
    
    def plot(noIte):
        population=main()[1]
        x = np.array([x.Fitness for x in population])
        y = np.power([i for i in range()])
        plt.errorbar(x, y, linestyle='None', marker='^')
        plt.show()
        
        
        
        
        
        
        
        
        
        