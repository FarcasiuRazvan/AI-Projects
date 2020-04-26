'''
Created on Mar 27, 2019

@author: Wolf
'''

from random import randint
ind=[]
for i in range(0,30):
    ind.append(0)
    
print(ind)

'''
def readFromFile():
        f=open("input.txt","r")
        line= f.readline().strip()
        table=[]
        n=int(line[0])
        for i in range(0,n):
            line=f.readline().strip()
            attrs=line.split(" ")
            table.append([])
            for j in range(0,n):
                table[i].append(int(attrs[j]))
        
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

cit=readFromFile()
n=cit[0]
table=cit[1]
t=cit[2]
noIteratii=cit[3]
dimPopulation=cit[4]
pM=cit[5]
print(cit)
'''


'''
n=6
table=[[0,1,0,0,0,1],[1,0,1,0,1,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,1,0,1,0,1],[1,0,0,0,1,0]]
t=2
noIteratii=1000
dimPopulation=100
pM=0.01
'''