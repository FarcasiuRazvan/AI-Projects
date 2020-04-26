'''
Created on Apr 15, 2019

@author: Wolf
'''

class problem(object):
    '''
    classdocs
    '''


    def __init__(self, file_name):
        '''
        Constructor
        '''
        self.filename=file_name
        self.words=[]
        self.trace=[]
        self.loadProblem()
        print("words: ",self.words)
    
    def loadProblem(self):
        '''
        reading the parameters
        '''
        f=open(self.filename,"r")
        self.words=[line.strip(" ").strip("\n") for line in f]
        self.words=self.words+self.get_column_words(self.words)
        self.n=len(self.words)
        f.close()
        
        for i in range(0,self.n):
            self.trace.append([])
            for j in range(0,self.n):
                if j>=i:
                    self.trace[i].append(1)
                else:
                    self.trace[i].append(0)
        
    def get_column_words(self,words):
        return ["".join([words[row][col] for row in range(len(words))]) for col in range(len(words[0]))]
        
        
        
        
        
        
        
        
        