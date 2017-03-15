#This file calculates numerical gradient of the neural network system.

import numpy as np
from NeuralNets import NeuralNets

class NumericalGradient(object):
    def __call__(self):
        return self

    def __init__(self):
        print "NumericalGradient"


    def computeNumericalGradient(self, n, X, y):
        paramsInitial = n.getParams()
        numGrad = np.zeros(paramsInitial.shape)
        perturb = np.zeros(paramsInitial.shape)
        e = 1e-4

        for p in range(len(paramsInitial)):
            # Set perturbation vector
            perturb[p] = e
            n.setParams(paramsInitial + perturb)
            loss2 = n.costFunction(X, y)

            n.setParams(paramsInitial - perturb)
            loss1 = n.costFunction(X, y)

            # Compute Numerical Gradient
            numGrad[p] = (loss2 - loss1) / (2 * e)

            # Return the value we changed to zero:
            perturb[p] = 0

        # Return Params to original value:
        n.setParams(paramsInitial)

        return numGrad