import numpy as np

n,m,p = map(int, input().split())

# First way
arr1 = np.array([input().split() for _ in range(n)], int)
arr2 = np.array([input().split() for _ in range(m)], int)

conc = np.concatenate((arr1, arr2), axis=0)
print(conc)


# Second way
arr = np.array([input().split() for _ in range(n+m)], int)

print(arr)

