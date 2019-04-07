# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_n = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

union = set_n.union(set_b)
print(len(union))