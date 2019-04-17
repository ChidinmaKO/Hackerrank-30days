# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in itertools.product(A, B):
    print(i, end=" ")

# Second way, Using unpacking.
A = map(int, input().split())
B = map(int, input().split())

print(*itertools.product(A,B))