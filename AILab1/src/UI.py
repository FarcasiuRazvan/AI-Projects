'''
Created on Mar 10, 2019

@author: Wolf
'''

from state import State
from problem import Problem
from controller import Controller
import time


initialState=State()
initialState.setValues([[3,0,0,2],[0,1,4,0],[1,2,0,4],[0,3,2,1]])
validState=State()
validState.setValues([[3,4,1,2],[2,1,4,3],[1,2,3,4],[4,3,2,1]])
test9x9=State()
test9x9.setValues([[0,0,3,0,6,9,0,0,0],[0,5,4,0,0,3,0,6,9],[9,2,6,5,1,4,3,8,7],[1,7,5,9,3,8,6,2,4],[3,8,2,4,5,6,9,7,1],[6,4,9,1,2,7,8,5,3],[5,9,7,6,4,1,2,3,8],[2,3,1,8,7,5,4,9,6],[4,6,8,3,9,2,7,1,5]])
test9x9copy=State()
test9x9copy.setValues([[8,1,3,7,6,9,5,4,2],[7,5,4,2,8,3,1,6,9],[9,2,6,5,1,4,3,8,7],[1,7,5,9,3,8,6,2,4],[3,8,2,4,5,6,9,7,1],[6,4,9,1,2,7,8,5,3],[5,9,7,6,4,1,2,3,8],[2,3,1,8,7,5,4,9,6],[4,6,8,3,9,2,7,1,5]])

class UI:
    
    def __init__(self):
        pass
    def printMainMenu(self):
        s = ''
        s += "0 - exit \n"
        s += "1 - find a path with BFS \n"
        s += "2 - find a path with GBFS\n"
        print(s)
        
    def findPathBFS(self):
        probleme=Problem(initialState)
        ctrl=Controller(probleme)
        startClock = time.time()
        print(ctrl.BFS())  
        print('execution time = ',time.time()-startClock, " seconds" )
        
    def findPathGBFS(self):
        probleme=Problem(initialState)
        ctrl=Controller(probleme)
        startClock = time.time()
        print(ctrl.Gbfs())  
        print('execution time = ',time.time()-startClock, " seconds" )
   
    def run(self):
        runM=True
        self.printMainMenu()
        while runM:        
            try: 
                command = int(input(">>"))
                if command == 0:
                    runM = False
                elif command == 1:
                    self.findPathBFS()
                elif command == 2:
                    self.findPathGBFS()         
                else:
                    print('invalid command')
            except ValueError:
                print('invalid command')
