import numpy as np

n,m = map(int, input().split())

i = np.array([input().split() for _ in range(n)], int)

result = np.prod(np.sum(i, axis=0))
print(result)