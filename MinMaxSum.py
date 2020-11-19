#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minVal = sum(arr[:4])
    maxVal = sum(arr[1:])
    print(minVal, maxVal)
    pass
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(arr)
    miniMaxSum(arr)
