import numpy as np 

n,m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

add = a+b
sub = a-b
mult = a*b
intdiv = a//b
mod = a%b
power = a**b

print(add, sub, mult, intdiv, mod, power, sep='\n')