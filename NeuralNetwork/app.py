#This is a main application file
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import time
from NeuralNets import NeuralNets
from Trainer import Trainer
from NumericalGradient import NumericalGradient

#Add all functions here!

#Ok, what is sigmoid activation function
def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoidDerivative(z):
    #Derivative of sigmoid function
    return np.exp(-z)/((1+np.exp(-z)) ** 2)

def drawSigmoidDerivative(testValue):
    plt.plot(testValues, sigmoid(testValues), linewidth=2)
    plt.plot(testValues, sigmoidDerivative(testValues), linewidth=2)
    plt.grid(1)
    plt.legend(['sigmoid', 'sigmoidDerivative'])
    plt.show()

def plotCost(x,y):
    plt.title('After optimization - Iterations vs Cost')
    plt.plot(x)
    plt.plot(y)
    plt.grid(1)
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.legend(["T.J", "t.testJ"])
    plt.show()

def plotSigmoid(z):
    testInput = np.arange(-z, z, 0.01)
    plt.plot(testInput, sigmoid(testInput), linewidth = 2)
    plt.grid(1)
    plt.show()

testValues = np.arange(-5, 5, 0.01)
#drawSigmoidDerivative(testValues)

plt.interactive(False)

#Input data
X = np.array(([3, 5], [5, 1], [10, 2]), dtype=float)
y = np.array(([75], [82], [93]), dtype=float)

print "Input values : "
print X

print "Output values : "
print y

#Normalization of input values
X = X/np.amax(X, axis=0)
y = y/100 #100 is the max value of output list

#Display shapes of input and output values
print "Shapes of input and output values"
print X.shape, y.shape

#Training without optimization
print "Training without optimization!"
NN_try = NeuralNets(Lambda=1)
yHat = NN_try.forward(X)
print yHat
print y

#Plot to show the difference
plt.title('Before optimization!')
plt.bar([0, 1, 2], y, width=0.35, alpha=0.8)
plt.bar([0.35, 1.35, 2.35], yHat, width=0.35, color='r', alpha=0.8)
plt.grid(1)
plt.legend(['y', 'yHat'])
plt.show()

#Display total running time for 1000 size of axis
weightsToTry = np.linspace(-5, 5, 1000)
costs = np.zeros(1000)
startTime = time.clock()
for i in range(1000):
    NN_try.W1[0, 0] = weightsToTry[i]
    yHat = NN_try.forward(X)
    costs[i] = 0.5 * sum((y-yHat)**2)

endTime = time.clock()

print "Elapsed time for 1000 size is :" + str(endTime-startTime)

#The plot of weight vs cost
plt.title('Weights vs Costs for 1000 size')
plt.plot(weightsToTry, costs)
plt.grid(1)
plt.xlabel('Weight')
plt.ylabel('Costs')
plt.show()


#Display total running time for 1000x1000 size of axis
weightsToTry = np.linspace(-5, 5, 1000)
costs = np.zeros((1000,1000))
startTime = time.clock()
for i in range(1000):
    NN_try.W1[0, 0] = weightsToTry[i]
    NN_try.W1[0, 1] = weightsToTry[i]
    yHat = NN_try.forward(X)
    costs[i] = 0.5 * sum((y-yHat)**2)

endTime = time.clock()

print "Elapsed time for 1000x1000 size is :" + str(endTime-startTime)

#The plot of weight vs cost
plt.title('Weights vs Costs for 1000x1000 size')
plt.plot(weightsToTry, costs)
plt.grid(1)
plt.xlabel('Weight')
plt.ylabel('Costs')
plt.show()


#Training Data:
trainX = np.array(([3,5], [5,1], [10,2], [6,1.5], [1,9],[2,6], [4, 4], [4,6], [8,4]), dtype=float)
trainY = np.array(([75], [82], [93], [70], [50], [62], [70], [74], [100]), dtype=float)

#Testing Data:
testX = np.array(([4, 5.5], [4.5,1], [9,2.5], [6, 2]), dtype=float)
testY = np.array(([70], [89], [85], [75]), dtype=float)

#Normalize:
trainX = trainX/np.amax(trainX, axis=0)
trainY = trainY/100 #Max test score is 100

#Normalize by max of training data:
testX = testX/np.amax(trainX, axis=0)
testY = testY/100 #Max test score is 100

#Training starts from here...

#New input X, and y

NN = NeuralNets(Lambda = 0.0001)

numGrad = NumericalGradient().computeNumericalGradient(NN, trainX, trainY)
grad = NN.computeGradients(X, y)
print np.linalg.norm(grad-numGrad)/np.linalg.norm(grad+numGrad)

T = Trainer(NN)
T.train(trainX, trainY, testX, testY)

#Plotting Cost during iteration
plotCost(T.J, T.testJ)