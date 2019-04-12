# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
for _ in range(int(input())):
    q = set(map(int, input().split()))
    if not a > q:
        print('False')
        exit()
print('True')