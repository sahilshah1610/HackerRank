import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    print(a, d)
    count = 0
    while count != d:
        firstValue = a[0]
        for x in range(len(a)-1):
            a[x] = a[x+1]
        a[-1] = firstValue
        count+=1



a = [1, 2, 3, 4, 5]
d = 4
rotLeft(a, d)