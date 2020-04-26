'''
Created on Mar 27, 2019

@author: Wolf
'''

class problem(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.params=self.readFromFile()
        
    def readFromFile(self):
        f=open("data02.txt","r")
        line= f.readline().strip()
        table=[]
        n=int(line[0])
        for i in range(0,n):
            line=f.readline().strip()
            attrs=line.split(" ")
            table.append([])
            for j in range(0,n):
                table[i].append(int(attrs[j]))
        f.close()
        f=open("param.txt","r")
        line=f.readline().strip()
        t=int(line.split(" ")[0])
        
        line=f.readline().strip()
        noIteratii=int(line.split(" ")[0])    
        
        line=f.readline().strip()
        dimPopulation=int(line.split(" ")[0])
        
        line=f.readline().strip()
        pM=float(line.split(" ")[0])
        f.close()
        return [n,table,t,noIteratii,dimPopulation,pM]