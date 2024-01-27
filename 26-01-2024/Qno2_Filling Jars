'''
Animesh has n empty candy jars, numbered from 1 to n, with infinite capacity. He performs m operations.
Each operation is described by 3 integers,a ,b , and k. Here, a and b are indices of the jars, and k is the number of candies to be added inside each jar whose index lies between a and b (both inclusive).
Can you tell the average number of candies after m operations?
Sample Input

STDIN       Function
-----       --------
5 3         n = 5, operations[] size = 3
1 2 100     operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
2 5 100
3 4 100
Sample Output

160
Explanation

Initially each of the jars contains 0 candies

0 0 0 0 0  
First operation:

100 100 0 0 0  
Second operation:

100 200 100 100 100  
Third operation:

100 200 200 200 100  
Total = 800, Average = 800/5 = 160
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY operations
#

def solve(n, operations):
    # Write your code here
    array = [0] * n

    for a, b, k in operations:
        for i in range(a - 1, b):
            array[i] += k

    average = int(sum(array) / n)
    return average

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    fptr.write(str(result) + '\n')

    fptr.close()
