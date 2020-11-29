#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    
    # Another Solution
    # shifted = arr[d % n:] + arr[:d % n]
    # for num in shifted:
    #     print(num, end=' ')

    return (arr[d:] + arr[:d])


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, d = map(int, input().split())
    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
