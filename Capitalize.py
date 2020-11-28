#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    splitText = s.split()
    for x in splitText:
        s = s.replace(x, x.capitalize())
    return s


if __name__ == '__main__':
    s = input()
    result = solve(s)


