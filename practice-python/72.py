import numpy as np 

# a,b = [np.array([input().split()], int) for _ in range(2)]

a = np.array(input().split(), int)
b = np.array(input().split(), int)


inner = np.inner(a,b)
outer = np.outer(a,b)
print(inner, outer, sep='\n')