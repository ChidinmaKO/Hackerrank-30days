import numpy as np 

n = int(input())
a = np.array([input().split() for _ in range(n)], float)
det = np.linalg.det(a)

print(round(det, 2))