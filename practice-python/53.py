# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = input()

for x,c in groupby(s):
    # print the length of the character(how many time it occures) 
    # and the integer
    print((len(list(c)), int(x)), end=' ')
    # using unpacking
    print(*[(len(list(c)), int(x))], end=' ')
