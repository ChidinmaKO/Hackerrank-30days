# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

s,k = input().split()

for j in sorted(itertools.permutations(s, int(k))):
    result = ''.join(j)
    print(result)