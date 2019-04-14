# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
num_custs = int(input())

earnings = 0

for i in range(num_custs):
    size,price = map(int, input().split())
    if shoe_sizes[size]:
        earnings += price
        shoe_sizes[size] -= 1

print(earnings)

# Without the Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT

num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_custs = int(input())

earnings = 0

for i in range(num_custs):
    size,price = map(int, input().split())
    if size in shoe_sizes:
        earnings += price
        shoe_sizes.remove(size)

print(earnings)