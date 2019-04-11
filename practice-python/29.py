# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
set_e = set(map(int, input().split()))

f = int(input())
set_f = set(map(int, input().split()))

sym_diff = set_e.symmetric_difference(set_f)
print(len(sym_diff))
