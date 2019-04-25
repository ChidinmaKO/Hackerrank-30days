import numpy as np 

# a tuple is needed here
integers = tuple(map(int, input().split()))

# recall that the default type is float
zeros = np.zeros(integers, int)
ones = np.ones(integers, int)

print(zeros, ones, sep='\n')


