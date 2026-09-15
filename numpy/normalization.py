import numpy as np

rng = np.random.default_rng(0)

X = rng.normal(size=(1000, 5))

means = X.mean(axis=0)  
stds  = X.std(axis=0)   

out = (X - means) / stds

assert np.allclose(out.mean(axis=0), 0, atol=1e-12)
assert np.allclose(out.std(axis=0), 1, atol=1e-12)