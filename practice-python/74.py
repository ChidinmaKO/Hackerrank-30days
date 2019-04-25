import numpy as np 
np.set_printoptions(legacy='1.13')

n,m = map(int, input().split())
eye = np.eye(n,m, dtype=float)
print(eye)