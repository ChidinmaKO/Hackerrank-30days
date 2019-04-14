# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
result = []
for _ in range(x):
    result.append(map(float, input().split()))

for i in zip(*result):
    print(sum(i)/len(i))