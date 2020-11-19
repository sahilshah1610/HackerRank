#!/bin/python

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.

def plusMinus(arr):
    valuePos = 0
    valueNeg = 0
    valueZero = 0
    for num in arr:
        if num > 0:
            valuePos += 1
        elif num < 0:
            valueNeg += 1
        else:
            valueZero += 1
    print("{0:.6f}".format((valuePos / len(arr))))
    print("{0:.6f}".format((valueNeg / len(arr))))
    print("{0:.6f}".format((valueZero / len(arr))))


if __name__ == '__main__':
    n = int(input())
    print(n)
    arr = list(map(int, input().rstrip().split()))
    #arr = [-4, 3, -9 ,0, 4, 1]
    plusMinus(arr)