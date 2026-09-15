import numpy as np

rng = np.random.default_rng(0)
A = rng.normal(size=(200000,1 ,3))
B = rng.normal(size=(1,20000, 3))

C = A * B

print(C)

# This program creates the following memory error
# numpy._core._exceptions._ArrayMemoryError: 
# Unable to allocate 89.4 GiB for an array with shape (200000, 20000, 3) and data type float64
# therefore, intermediate array which created in the middle of broadcasting calculation can be run out of memory 