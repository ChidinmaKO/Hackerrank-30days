# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = complex(input())
result = cmath.polar(z)

print(*result, sep='\n')