# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
set_e = set(map(int, input().split()))
f = int(input())
set_f = set(map(int, input().split()))

diff = set_e.difference(set_f)
print(len(diff))