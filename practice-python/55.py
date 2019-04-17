# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# The first line contains 2 space separated integers k and m.
k,m = map(int, input().split())

# The next k lines each contains an integer ni, denoting the number of elements in the ith list, followed by ni space separated integers denoting the elements in the list.
n = [list(map(int, input().split()))[1:] for _ in range (k)]

r = map(lambda x: sum(i**2 for i in x)%m, product(*n))
print(max(r))