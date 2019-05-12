# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for i in range(t):
    s = str(input())
    even = s[::2]
    odd = s[1::2]
    result = "".join(even),"".join(odd)
    print(*result)

# Shorter and more pythonic in my opinion
for _ in range(int(input())):
    s = input()
    print(*["".join(s[::2]),"".join(s[1::2])])