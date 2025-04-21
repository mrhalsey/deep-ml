import numpy as np

def kernel_function(x1, x2):
	# Your code here
    if len(x1) != len(x2):
        return None
    prod = 0
    for i in range(len(x1)):
        prod += x1[i] * x2[i]
    return prod
