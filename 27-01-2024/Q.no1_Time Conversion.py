'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # extract am or pm
    slice=s[-2:]
    # extract time[07:05:45] and convert it into list
    sliced_time=s[:8]
    split_time=sliced_time.split(':')
    # check HH == 12 or not.
    if split_time[0]=='12':
        # check am or pm then if its am convert 12 into 00 else return the original time
        if slice=='AM':
            split_time[0]='00'
            result=':'.join(split_time)
            return result
        else:
            result=':'.join(split_time)
            return result
    else:
        # check am or pm if its pm add 12 to HH else return original time
        if slice=='PM':
            a=int(split_time[0])
            b=a+12
            split_time[0]=str(b)
            result=':'.join(split_time)
            return result
        else:
            result=':'.join(split_time)
            return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
