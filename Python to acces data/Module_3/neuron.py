import numpy as np

# First we set the state of the network
σ = np.tanh
w1 = 1.3
b1 = -0.1


# Then we define the neuron activation.
def a1(a0):
    return σ(w1 * a0 + b1)


# Finally let's try the network out!
# Replace x with 0 or 1 below,
x = 0
a1(x)
print(a1)
