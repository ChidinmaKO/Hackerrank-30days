# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations, takewhile

n = int(input())
l = input().split()
k = int(input())

C = list(combinations(l, k))

# why did filter work here instead of takewhile. This is because 
# takewhile stops as soon as the predicate turns false while filter 
# goes through the entire input iterator.

# f = takewhile(lambda c: 'a' in c, C)
f = filter(lambda c: 'a' in c, C)
result = "{:.3}".format(len(list(f))/ len(C))
print(result)