'''
Created on Mar 27, 2019

@author: Wolf
'''
from Problem import *
from Population import population
from Algorithm import algorithm
from Individ import individ
from random import randint
import statistics
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass

def main():
    prb=problem()
    cit=prb.params
    n=cit[0]
    table=cit[1]
    t=cit[2]
    noIteratii=cit[3]
    dimPopulation=cit[4]
    pM=cit[5]


    pop=[]
    cont=0

    '''
    Create the population.
    '''
    while cont<dimPopulation:
        cont+=1
        indiv=[]
        for i in range(0,n):
            indiv.append(0)
        leng=randint(1,n)
        cleng=leng
        while leng>0:
            i=randint(0,n-1)
            if indiv[i]==0:
                indiv[i]=1
                leng-=1
        ind=individ(indiv,cleng,table,t)
        pop.append(ind)
        
    p=population(dimPopulation,pop)


    '''
    Running the algorithm
    '''
    alg=algorithm()
    for i in range(0,noIteratii):
        p=alg.iteration(table,p,t,pM)
    p.validate(n)
    
    '''
    Getting the best result.
    '''
    result=sorted(p.getPopulation(),key=lambda x:x.getLength(), reverse=False )
    print(len(result))
    for i in range(0,1):
        print(result[i].getList(),result[i].getLength(),result[i].fitness(table,t))
    
    
    '''
    Plot.
    '''
    pl=[p.getLength() for p in result]
    plot(pl)
    return [result[0].fitness(table,t),result]
    

def tests():
    minValues = [main()[0] for x in range(30)]
    print("Mean:", statistics.mean(minValues),
            "Stdev", statistics.stdev(minValues))
    
def plot(result):
    print(result)
    x = np.array([x for x in result])
    y = np.array([i for i in range(0,len(result))])
    plt.errorbar(y, x, linestyle='None', marker='^')
    plt.show()

#main()
tests()  
    