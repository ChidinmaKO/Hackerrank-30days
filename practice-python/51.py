# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, k = input().split()

# so it doesn't return 0 combinations. We need 1 to k+1 combinations
for l in range(1, int(k)+1):
    for p in combinations(sorted(s), l):
        result = ''.join(p)
        print(result)

# Second way. Sorting early on.
q= input().split()
s,k = sorted(q[0]), int(q[1])

# so it doesn't return 0 combinations. We need 1 to k+1 combinations
for l in range(1, k+1):
    for p in combinations(s, l):
        result = ''.join(p)
        print(result)