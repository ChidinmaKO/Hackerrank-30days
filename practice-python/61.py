# Enter your code here. Read input from STDIN. Print output to STDOUT

# Using collections.deque
from collections import deque
# d = deque()

n = int(input())

for _ in range(n):
    t = int(input())
    side_lens = deque(map(int, input().split()))
    result = "Yes"
    if max(side_lens) not in (side_lens[0], side_lens[-1]):
        result = "No"
    print (result)

# Using while loops

n = int(input())

for _ in range(n):
    t = int(input())
    x = list(map(int, input().split()))
    l = len(x)
    i = 0
    while i < l - 1 and x[i] >= x[i+1]:
        i += 1
    while i < l - 1 and x[i] <= x[i+1]:
        i += 1
    if i == l - 1:
        print ("Yes")
    else:
        print ("No")
