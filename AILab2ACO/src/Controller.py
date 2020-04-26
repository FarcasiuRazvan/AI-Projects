'''
Created on Apr 15, 2019

@author: Wolf
'''
from random import randint
import statistics
import numpy as np
import matplotlib.pyplot as plt

from Problem import problem
from copy import deepcopy
from Ant import ant
from random import *

class controller(object):
    '''
    classdocs
    '''

    def __init__(self, data_file_path,params_file_path):
        '''
        Constructor
        '''
        self.problem=problem(data_file_path)
        self.noRuns=0
        self.noGenes=0
        self.local_pheromone_increase=0
        self.global_pheromone_increase=0
        self.Evaporation=0
        self.bestProbability=0
        self.load_parameters(params_file_path)
        self.population=[]
        self.noSteps=len(self.problem.words)//2-1
        
        self.trace=deepcopy(self.problem.trace)
        
    def iteration(self):
        for word in range(0,len(self.problem.words)):
            Ant= ant()
            Ant.update(word)
            self.population.append(Ant)
        
        for i in range(0,self.noSteps):
            for Ant in self.population:
                current_word=Ant.solution[len(Ant.solution)-1]
                
                neighbours=self.get_neighbours(Ant, current_word)
                
                if len(neighbours)!=0:
                    if(random() <self.bestProbability):
                        next_word= self.get_best_neighbour(neighbours, current_word)
                    else:
                        next_word= choice(neighbours)
                    
                    Ant.update(next_word)

        best_ant=self.get_best_ant()
        
        if best_ant!=None:
            self.spread_pheromones(best_ant)
            
    def spread_pheromones(self,ant):
        x=ant.solution[0]
        for y in ant.solution[1:]:
            self.trace[x][y]=self.local_pheromone_increase
            x=y
    
    def get_neighbours(self,ant,current_word):
        neighbours=self.trace[current_word]
        result=[]
        for i in range(0,len(neighbours)):
            if neighbours[i]==1 and i not in ant.solution:
                result.append(i)

        return result
        
    def get_best_ant(self):
        population=sorted(self.population, key=lambda Ant: Ant.fitness(self.problem))
        if(population[0]!=population[1]):
            return population[0]
        return None
    
    def get_best_ant_plot(self):
        population=sorted(self.population, key=lambda Ant: Ant.fitness(self.problem))
        result=[p.fitness(self.problem) for p in population]
        self.plot(result)
    
    def get_best_neighbour(self, neighbours, current_word):
        next_word = neighbours.pop()
        for neighbour in neighbours: 
            if self.trace[current_word][next_word] < self.trace[current_word][neighbour]:
                next_word = neighbour
            return next_word
        return next_word
        
    def run(self):
        for i in range(self.noGenes):
            self.iteration()
            best_ant = self.get_best_ant()
            if best_ant.fitness(self.problem) == 0: 
                self.get_best_ant_plot()
                return best_ant

            self.evaporation()
            self.population = [] 
            self.trace = deepcopy(self.problem.trace)
        return best_ant
    
    def evaporation(self):
        self.decrease_pheromones_on_all_edges(self.Evaporation)

    def decrease_pheromones_on_all_edges(self, coef):
        for i in range(0,self.problem.n):
            for j in range(0,self.problem.n):
                self.trace[i][j] -= coef
    
    def spread_pheromones_on_path(self, best_ant):
        ant = deepcopy(best_ant)
        x1 = ant.soution.pop()
        while len(ant.solution) > 0:
            x2 = ant.solution.pop()
            self.trace[x1][x2]=self.global_pheromone_increase
            x1 = x2
    
    def load_parameters(self, params_file_name):
        with open(params_file_name, 'r') as file:
            
            line = file.readline().strip()
            self.noRuns = int(line.replace("number of runs:",""))
            
            line = file.readline().strip()
            self.noGenes = int(line.replace("number of generations:",""))
            
            line = file.readline().strip()
            self.local_pheromone_increase = float(line.replace("local pheromone increase:",""))
            
            line = file.readline().strip()
            self.global_pheromone_increase = float(line.replace("global pheromone increase:",""))
            
            line = file.readline().strip()
            self.Evaporation = float(line.replace("evaporation coefficient:",""))
            
            line = file.readline().strip()
            self.bestProbability = float(line.replace("probability for best:",""))
       
        
    def tests(self):
        minValues = []
        for i in range(30):
            self.iteration()
            best_ant = self.get_best_ant()
            if best_ant.fitness(self.problem)!=None:
                minValues.append(best_ant.fitness(self.problem))

            self.evaporation()
            self.population = [] 
            self.trace = deepcopy(self.problem.trace)
        print(minValues)
        print("Mean:", statistics.mean(minValues),
              "Stdev", statistics.stdev(minValues))
    
    def plot(self,result):
        print(result)
        x = np.array([x for x in result])
        y = np.array([i for i in range(0,len(result))])
        plt.errorbar(y, x, linestyle='None', marker='^')
        plt.show()
        
        
        
        
        
        
        
        
        
        