'''
Cities on a map are connected by a number of roads. The number of roads between each city is in an array and city 0 is the starting location.
The number of roads from city 0 to city 1 is the first value in the array, from city 1 to city 2 is the second, and so on.
How many paths are there from city 0 to the last city in the list, modulo 1234567?

Example
n=4
routes=[3,4,5]
There are 2 roads to city 1, 4 roads to city 2 and 5 roads to city 3. The total number of roads is 3x4x5%1234567=60 .
Sample Input

2
3
1 3
4
2 2 2
Sample Output

3
8
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectingTowns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY routes
#

def connectingTowns(n, routes):
    # Write your code here
    tot_route=1
    for route in routes:
        tot_route=(tot_route*route)%1234567
    return tot_route

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
