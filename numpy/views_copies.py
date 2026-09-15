
import numpy as np

rng = np.random.default_rng(0)
arr = rng.random(10)
original = arr.copy()
# print(f" first {arr}")

sliced = arr[2:5]
sliced[:] = 99          # what happened to arr?


masked = arr[arr > 0.5]
masked[:] = -1          # what happened to arr this time?



print(np.shares_memory(masked, original))

# Notes
"""
View is just a copy of array but connected or shared memory with original one
whereas, Copy is completely different array from it is copied 
and slice is a view of array but not boolean indexing 
"""