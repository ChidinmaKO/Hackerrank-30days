#!/bin/python3

# import math
# import random
# import re
# import sys
# Method 1
import os
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_code = "%a %d %b %Y %H:%M:%S %z"
    t1 = dt.strptime(t1, format_code)
    t2 = dt.strptime(t2, format_code)
    td = str(int(abs((t1-t2).total_seconds())))
    return(td)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')
    fptr.close()



# Method 2

from datetime import datetime as dt

t = int(input())
format_code2 = "%a %d %b %Y %H:%M:%S %z"

for i in range(t):
    t1 = dt.strptime(input(), format_code2)
    t2 = dt.strptime(input(), format_code2)
    td2 = int(abs(t1-t2).total_seconds())
    print(td2)