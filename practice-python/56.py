# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
cols = input().split()
grades = namedtuple("grades", cols)

marks = [int(grades._make(input().split()).MARKS) for _ in range(n)]
    
average = sum(marks) / len(marks)
print(average)