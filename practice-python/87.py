# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan2, degrees
ab = int(input())
bc = int(input())

# atan2 returns the arc tangent of (ab/bc) in radians
mbc_radians = atan2(ab, bc)
# convert the radians to degrees and round up
mbc_degrees = round(degrees(mbc_radians))
# str and int can't be concatenated so convert the rounded mbc_degrees to str.
print(str(int(mbc_degrees))+ "°")