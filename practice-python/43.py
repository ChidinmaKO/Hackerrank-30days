# Enter your code here. Read input from STDIN. Print output to STDOUT
import re #python module for regex

t = int(input())

for _ in range(t):
    result = True
    try:
        re.compile(input())
    except re.error:
        result = False
    print(result)