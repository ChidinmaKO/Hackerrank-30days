# Enter your code here. Read input from STDIN. Print output to STDOUT
# Using OrderedDict alone
from collections import OrderedDict

n = int(input())
words = OrderedDict()

for _ in range(n):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())

from collections import Counter, OrderedDict

n = int(input())

# Using the OrderedCounter class
# from collections import Counter, OrderedDict
# n = int(input())
# class OrderedCounter(Counter, OrderedDict):
#     pass

# words = OrderedCounter(input() for _ in range(n))

# print(len(words))
# print(*words.values())