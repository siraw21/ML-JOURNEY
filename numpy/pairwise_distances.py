import numpy as np

# Double loop version
rng = np.random.default_rng(0)
A = rng.normal(size=(1000, 3))
B = rng.normal(size=(500, 3))

loop_distances = np.zeros((1000,500))

for i,a in enumerate(A):
   for j,b in enumerate(B):
    dist = np.sqrt(np.sum(np.square(b - a)))
    loop_distances[i,j] = dist

# print(loop_distances)



# Broadcasting Version 
rng = np.random.default_rng(0)

A = rng.normal(size=(1000, 3))
B = rng.normal(size=(500, 3))


diff = A[:, np.newaxis, :] - B[np.newaxis, :, :]


broadcast_distances = np.sqrt(np.sum(np.square(diff), axis=2))

# print(broadcast_distances)
# print(broadcast_distances.shape)


are_close = np.allclose(loop_distances, broadcast_distances, atol=1e-9)

print(are_close)