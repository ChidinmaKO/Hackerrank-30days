# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

for _ in range(t):
    n = str(input())
    regex_pattern = re.match(r'^[-+]?[0-9]*\.[0-9]+$', n)
    result = bool(regex_pattern)
    print(result)