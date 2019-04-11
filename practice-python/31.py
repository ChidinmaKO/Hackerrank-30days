# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
set_A = set(map(int, input().split()))
N = int(input())
B = []
V = []

for i in range(N):
    B = input().split()
    V = set(map(int, input().split()))
    if 'intersection_update' in B:
        set_A.intersection_update(V)
    elif 'update' in B:
        set_A.update(V)
    elif 'symmetric_difference_update' in B:
        set_A.symmetric_difference_update(V)
    elif 'difference_update' in B:
        set_A.difference_update(V)
print(sum(set_A))
