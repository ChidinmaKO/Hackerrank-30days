import numpy as np

n,m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)

result = np.max(np.min(a, axis=1))
print(result)
