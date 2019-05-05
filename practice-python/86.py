# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

letters = string.ascii_letters
odd_num = '13579'
even_num = '02468'

s = input()

sorted_str = sorted(s, key=(letters + odd_num + even_num).index)
print(*sorted_str, sep='')