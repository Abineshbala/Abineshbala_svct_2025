'''
You will be given a list of integers,arr , and a single integer k. You must create an array of length k from elements of arr such that its unfairness is minimized.
Call that array arr. Unfairness of an array is calculated as
max(arr)-min(arr)
Sample Input 0

7
3
10
100
300
200
1000
20
30
Sample Output 0

20
Explanation 0

Here ;k=3 selecting the k integers 10,20,30, unfairness equals

max(10,20,30) - min(10,20,30) = 30 - 10 = 20

Sample Input 1

10
4
1
2
3
4
10
20
30
40
100
200
Sample Output 1

3
Explanation 1

Here ;k=4 selecting the 4 integers 1,2,3,4, unfairness equals

max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    min_unfairness = float('inf')

    for i in range(len(arr) - k + 1):
        current_unfairness = arr[i + k - 1] - arr[i]
        min_unfairness = min(min_unfairness, current_unfairness)
    
    return min_unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
