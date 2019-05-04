#!/bin/python3

import math
import os
import random
import re
import sys

def func(arr):
    return arr[k]

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in sorted(arr, key=func):
        print (*i)


# Using operator.itemgetter
from operator import itemgetter
n,m = list(map(int, input().split()))

arr = [[int(i) for i in input().split()] for _ in range(n)]

for i in sorted(arr, key=itemgetter(int(input()))):
    print (*i)
