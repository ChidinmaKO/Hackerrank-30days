n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(c):
    cmds = list(input().split())
    if cmds[0] == "pop":
        s.pop()
    elif cmds[0] == "remove":
        s.remove(int(cmds[-1]))
    elif cmds[0] == "discard":
        s.discard(int(cmds[-1]))
print(sum(s))