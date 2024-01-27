'''
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other.
If the sum of digits is equal for both numbers, then she thinks the smaller number is better. 
Given an integer, n, can you find the divisor of n that Kristin will consider to be the best?

Sample Input 0

12
Sample Output 0

6
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def best_divisor(number):
    best_div = 1
    max_digit_sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            digit_sum = sum(map(int, str(i)))
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
                best_div = i

    return best_div

if __name__ == '__main__':
    n = int(input().strip())
    print(best_divisor(n))
