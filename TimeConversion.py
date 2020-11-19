#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    convertedTime = ''
    splitText = s.split(':')
    if 'PM' in splitText[2]:
        if int(splitText[0]) < 12:
            convertedHour = int(splitText[0])+12
            splitText[2] = splitText[2].strip('PM')
            convertedTime = str(convertedHour) + ':' + splitText[1] + ':' + str(splitText[2])
        else:
            splitText[2] = splitText[2].strip('PM')
            convertedTime = str(splitText[0]) + ':' + splitText[1] + ':' + str(splitText[2])
    elif 'AM' in splitText[2]:
        if int(splitText[0]) >=12:
            convertedHour = int(splitText[0]) - 12
            splitText[2] = splitText[2].strip('AM')
            convertedTime = str(convertedHour) + '0:' + splitText[1] + ':' + str(splitText[2])
        else:
            splitText[2] = splitText[2].strip('AM')
            convertedTime = str(splitText[0]) + ':' + splitText[1] + ':' + str(splitText[2])
    return convertedTime
    #
    # Write your code here.
    #

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    #f.write(result + '\n')

    #f.close()
