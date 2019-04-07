# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_n = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

intersection = set_n.intersection(set_b)
print(len(intersection))