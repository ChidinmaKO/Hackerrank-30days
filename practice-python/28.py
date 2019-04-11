# Enter your code here. Read input from STDIN. Print output to STDOUT
# One way
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# exp1 = a**b
# exp2 = c**d
# print(exp1 + exp2)

# Better way
a,b,c,d = (int(input()) for _ in range(4))
print((a**b) + (c**d))

