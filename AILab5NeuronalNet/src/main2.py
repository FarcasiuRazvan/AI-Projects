from random import *
from numpy import *
from Layer import *
import statistics
import matplotlib.pyplot as plt
from ActivationFunctions import *

def readFromFile(filename):
    f = open(filename, 'r')
    input = []
    output = []
    for line in f:
        l=line.split(",")
        aux = []
        aux.append(float(l[0]))
        aux.append(float(l[1]))
        aux.append(float(l[2]))
        aux.append(float(l[3]))
        result = l[4].split("\n")[0]
        if result == "Move-Forward":
            output.append([1, 0, 0, 0, 0])
        if result == "Sharp-Right-Turn":
            output.append([0, 1, 0, 0, 0])
        if result == "Sharp-Left-Turn":
            output.append([0, 0, 1, 0, 0])
        if result == "Slight-Right-Turn":
            output.append([0, 0, 0, 1, 0])
        if result == "Slight-Left-Turn":
            output.append([0, 0, 0, 0, 1])
        input.append(aux)
    return input, output

def normData(arr):
    mi = min(arr)
    ma = max(arr)
    for i in range(0, len(arr)):
        arr[i] = (arr[i] - mi) / (ma - mi)
    return arr

def classify(o1, o2, o3, o4, o5):
    ma = max(o1, o2, o3, o4, o5)
    if ma == o1:
        return "Move-Forward"
    if ma == o2:
        return "Sharp-Right-Turn"
    if ma==o3:
        return "Sharp-Left-Turn"
    if ma==o4:
        return "Slight-Right-Turn"
    if ma==o5:
        return "Slight-Left-Turn"
    
def classifyNum(o1, o2, o3, o4, o5):
    return max(o1, o2, o3, o4, o5)

def main():
    input, output = readFromFile("sensor_readings_4.data")
    vector=[]
        
    layer0Weights = []
    layer0 = Layer(15, 4) 
    for neuron in layer0.neurons:
        layer0Weights.append(neuron.weights)
  
    layer1Weights = []
    layer1 = Layer(5, 15)
    for neuron in layer1.neurons:
        layer1Weights.append(neuron.weights)

    for i in range(0,1000):# len(input)):
#         layer0Weights = []
#         layer0 = Layer(15, 4) 
#         for neuron in layer0.neurons:
#             layer0Weights.append(neuron.weights)
#  
#         layer1Weights = []
#         layer1 = Layer(5, 15)
#         for neuron in layer1.neurons:
#             layer1Weights.append(neuron.weights)
        for j in range(0, 100):

            input[i] = normData(input[i])
            l0 = input[i]

            layer0WeightsT = array(layer0Weights).T
            layer1WeightsT = array(layer1Weights).T
            
            
            l1 = sigmoid(dot(input[i], layer0WeightsT))
            l2 = sigmoid(dot(l1, layer1WeightsT)) 
            
            
            l2_error = output[i] - l2
            l2_delta = l2_error * derivata(l2) 

            l1_error = dot(l2_delta, layer1Weights)
            l1_delta = l1_error * derivata(l1)
            
            #if j % 10 == 0:
            #print(l2)

    
            layer1Weights += dot(l2, l2_delta)
            layer0Weights += dot(l1, l1_delta)
        #if(max(l2_error))
        vector.append(max(l1_error))
            
        print(str(i + 1) + ": " + classify(l2_error[0], l2_error[1], l2_error[2],l2_error[3],l2_error[4]),max(l2_error))
        
    plot(vector)

def plot(result):
    print(result)
    x = array([x for x in result])
    y = array([i for i in range(0,len(result))])
    plt.errorbar(y, x)
    plt.show()
main()
