#!/bin/python3

import math
import os
import random
import re
import sys
def ifElse(n):
    list2to5 = [i for i in range(2, 6)]
    list6to20 = [i for i in range(6, 21)]
    ans = ''
    if n%2 != 0:
        ans = 'Weird'
    elif n%2 == 0 and n in list2to5:
        ans = 'Not Weird'
    elif n%2 == 0 and n in list6to20:
        ans = 'Weird'
    elif n%2 == 0 and n>20:
        ans = 'Not Weird'
    return ans



if __name__ == '__main__':
    n = int(input().strip())
    result = ifElse(n)
    print(result)