import numpy as np
# matmul can be used here too

n = int(input())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

result = np.dot(a,b)
print(result)