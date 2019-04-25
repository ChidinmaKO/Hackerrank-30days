import numpy as np 

p = list(map(float, input().split()))
x = int(input())
val = np.polyval(p,x)

print(val)