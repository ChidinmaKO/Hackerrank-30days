# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

k = int(input()) # size of each group
l = list(map(int, input().split())) # list of room numbers

# for key,value in Counter(l).items():
#     if value != k:
#         print(key)

# better way
result = ([key for key,value in Counter(l).items() if value != k])
print(*result)
