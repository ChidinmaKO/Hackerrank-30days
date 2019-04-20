# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
od = OrderedDict()

# Using rsplit()
for _ in range(n):
    # split the name & price from the right.
    name, price = input().rsplit(None, 1)
    # od ensures that they maintain their order
    # get the names, if non-existent, default value is 0, and the price
    od[name] = od.get(name, 0) + int(price)
    # Use .items() to return a list of all the names & prices of all the items
for name, price in od.items():
    print(name, price)

# Using rpartition()
# for _ in range(n):
#     # rpartition returns a tuple with 3 elements. So we need a dummy variable, space
#     name, space, price = input().rpartition(' ')
#     od[name] = od.get(name, 0) + int(price)
# for name, price in od.items():
#     print(name, price)