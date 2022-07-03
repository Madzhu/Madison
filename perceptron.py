import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_inputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weight = 2 * np.random.random((3, 1)) - 1

print(" ")
print(synaptic_weight)

input_layer = training_inputs
outputs