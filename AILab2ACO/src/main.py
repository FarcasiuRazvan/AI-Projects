from Controller import controller


data_file_path="words.txt"
params_file_path="parameters.txt"

controller=controller(data_file_path,params_file_path)

print("computing the solution")
'''
'''
best_ant=controller.run()
result=best_ant.getResult(controller.problem)
for i in result:
    print(i)
print("fitness ",best_ant.fitness(controller.problem))

'''
controller.tests()
'''
'''
controller.plot()
'''