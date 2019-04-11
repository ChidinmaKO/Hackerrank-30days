# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
country = [input() for i in range(n)]

distinct = len(set(country))
print(distinct)