import numpy as np 
# Using the set_printoptions helps with the formatting
np.set_printoptions(legacy='1.13')

n,m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)

mean = np.mean(a, axis=1)
var = np.var(a, axis=0)
std = np.std(a)

print(mean, var, std, sep='\n')