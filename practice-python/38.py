# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
L = input().split()
print(all([int(i) > 0 for i in L]) and any([i == i[::-1] for i in L]))