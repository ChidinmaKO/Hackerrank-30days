from collections import defaultdict

d = defaultdict(list)
group_a = []

n,m = map(int, input().split())

for i in range(n):
    d[input()].append(i+1)

for j in range(m):
    group_a = group_a + [input()]

for k in group_a:
    if k in d:
        print(' '.join(map(str, d[k])))
    else:
        print(-1)