'''
Created on Mar 10, 2019

@author: Wolf
'''


from UI import UI
'''
initialState=State()
initialState.setValues([[3,0,0,2],[0,1,4,0],[1,2,0,4],[0,3,2,1]])
validState=State()
validState.setValues([[3,4,1,2],[2,1,4,3],[1,2,3,4],[4,3,2,1]])
test9x9=State()
test9x9.setValues([[0,0,3,0,6,9,0,0,0],[0,5,4,0,0,3,0,6,9],[9,2,6,5,1,4,3,8,7],[1,7,5,9,3,8,6,2,4],[3,8,2,4,5,6,9,7,1],[6,4,9,1,2,7,8,5,3],[5,9,7,6,4,1,2,3,8],[2,3,1,8,7,5,4,9,6],[4,6,8,3,9,2,7,1,5]])
test9x9copy=State()
test9x9copy.setValues([[8,1,3,7,6,9,5,4,2],[7,5,4,2,8,3,1,6,9],[9,2,6,5,1,4,3,8,7],[1,7,5,9,3,8,6,2,4],[3,8,2,4,5,6,9,7,1],[6,4,9,1,2,7,8,5,3],[5,9,7,6,4,1,2,3,8],[2,3,1,8,7,5,4,9,6],[4,6,8,3,9,2,7,1,5]])
print(Problem(test9x9).isValid())
print(Problem(test9x9).heuristic())
print(Problem(test9x9).isLeaf())
'''
#PROBLEME LA EURISTICA SAU PROBLEME LA EXPAND, PROBABIL LA EXPAND, TREBUIE RESCRISA FUNCTIA !!!!!!

#print(initialState.getFrecv())

#probleme=Problem(initialState)
'''
print(probleme.getCurrent())
probleme.expand()
probleme.expand()
print(probleme.getCurrent())
newproblem=Problem(probleme.getCurrent())
print(newproblem.getCurrent())
newproblem.expand()
newproblem.expand()
newproblem.expand()
print(newproblem.getCurrent())
print(newproblem.isValid())
print(newproblem.heuristic())
print(newproblem.isLeaf())

probleme=Problem(initialState)
ctrl=Controller(probleme)
print(ctrl.Gbfs())
'''

ui=UI()
ui.run()
