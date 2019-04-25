import numpy as np 

n,m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)

t = np.transpose(a)
f = a.flatten()

print(t, f, sep='\n')