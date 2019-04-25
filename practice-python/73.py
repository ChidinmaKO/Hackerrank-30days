import numpy as np 
np.set_printoptions(legacy='1.13')

# a = np.array([input().split()], float)
a = np.array(input().split(), float)

floor = np.floor(a)
ceil = np.ceil(a)
rint = np.rint(a)

# print(*floor, *ceil, *rint, sep='\n')
print(floor, ceil, rint, sep='\n')
