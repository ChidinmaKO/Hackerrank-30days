from collections import Counter

s = input()
c = sorted(s)
cnt = Counter(c).most_common(3)

for k,v in cnt:
    print(k,v)

# using unpacking *
for i in cnt:
    print(*i)

# Using OrderedCounter class
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

cnt = OrderedCounter(sorted(input())).most_common(3)
for i in cnt:
    print(*i)

# Better way
[print(*i) for i in OrderedCounter(sorted(input())).most_common(3)]