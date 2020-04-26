'''
Created on May 3, 2019

@author: Wolf
'''
from Repository import repository
from fileinput import filename
from Interval import interval
from Figure import figure

class controller(object):
    '''
    classdocs
    '''


    def __init__(self, inputSyst,outputSyst,problem):
        '''
        Constructor
        '''
        
        self.__repo=repository(self.loadInputFromFileSystem(inputSyst))
        self.__table=self.loadProblemInput(problem)
        self.__outputFig=self.loadOutputFromFileSystem(outputSyst)
        '''
        the parameter X is in figure
        '''
    def loadInputFromFileSystem(self,filename):
        with open(filename, 'r') as file:
            
            line = file.readline().strip()
            noFigs = int(line.replace("number of figures:",""))
            figures=[]
            for i in range(0,noFigs):
                line = file.readline().strip()
                nameFig= line.replace("name of the figure:","")
                line = file.readline().strip()
                noIntervals= int(line.replace("number of intervals:",""))
                intervals=[]
                for j in range(0,noIntervals):
                    line = file.readline().strip().split(" ")
                    params=[]
                    for z in range(1,len(line)):
                        params.append(float(line[z]))
                    intervals.append(interval(params,line[0]))
                line = file.readline().strip()
                x= float(line.replace("figure value:",""))
                figures.append(figure(intervals,nameFig,x))
        return figures
    
    def loadOutputFromFileSystem(self,filename):
        with open(filename, 'r') as file:
            line = file.readline().strip()
            nameFig= line.replace("name of the figure:","")
            line = file.readline().strip()
            noIntervals= int(line.replace("number of intervals:",""))
            intervals=[]
            for j in range(0,noIntervals):
                line = file.readline().strip().split(" ")
                params=[]
                for z in range(1,len(line)):
                    params.append(float(line[z]))
                intervals.append(interval(params,line[0]))
        return figure(intervals,nameFig,0)
    
    def loadProblemInput(self,filename):
        table=[[""]]
        with open(filename, 'r') as file:
            line = file.readline().strip()
            rowNo= int(line)
            line=file.readline().strip().split(" ")
            for i in range(0,len(line)):
                table[0].append(line[i])
            for i in range(1,rowNo):
                table.append([])
                line=file.readline().strip().split(" ")
                for j in range(0,len(line)):
                    table[i].append(line[j])
                
        return table
    
    def getMaxFromTable(self):
        figures=self.__repo.getFigures()
        
        maxFigNames=[]
        intervs=self.__outputFig.getIntervals()
        for i in intervs:
            maxFigNames.append(i.getName())
        maxFigValues=[]
        for i in range(0,len(maxFigNames)):
            maxFigValues.append(-99999)
        
        miuFig1=figures[1].getMiu()
        for i in range(1,len(self.__table[0])):
            self.__table[0][i]=(self.__table[0][i],miuFig1[i-1])
        
        miuFig2=figures[0].getMiu()
        for i in range(1,len(self.__table)):
            self.__table[i][0]=(self.__table[i][0],miuFig2[i-1])
        
        for i in range(1,len(self.__table)):
            for j in range(1,len(self.__table[0])):
                x=-1
                for name in maxFigNames:
                    if name==self.__table[i][j]:
                        x=j-1
                if self.__table[0][j][1]<self.__table[i][0][1]: 
                    if self.__table[0][j][1]>maxFigValues[x]:
                        maxFigValues[x]=self.__table[0][j][1]
                else:
                    if self.__table[i][0][1]>maxFigValues[x]:
                        maxFigValues[x]=self.__table[i][0][1]
        
        result=[]
        for i in range(0,len(maxFigNames)):
            result.append((maxFigNames[i],maxFigValues[i]))
        
        return result
    
    def getV(self):
        '''
        getMaxFromTable
        self.__outputFig
        '''
        maxims=self.getMaxFromTable()
        outputParams=[]
        for i in range(0,len(maxims)):
            if maxims[i][1]>0:
                outputParams+=self.__outputFig.getIntervals()[i].getParams()
                
        suma=0
        sumProd=0
        for i in range(0,len(outputParams)):
            sumProd+=outputParams[i]*maxims[i%3][1]
            suma+=outputParams[i]
          
        return sumProd/suma
        