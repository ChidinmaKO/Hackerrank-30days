# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())

# Better way
for i in range(n):
    method, *args = input().split()
    getattr(d, method)(*args)
print(*d)

# First way
# for i in range(n):
    # method, *value = input().split()

    # if method == "append":
    #     d.append(*value)
    # if method == "appendleft":
    #     d.appendleft(*value)
    # if method == "pop":
    #     d.pop()
    # if method == "popleft":
    #     d.popleft()
# print(*d)