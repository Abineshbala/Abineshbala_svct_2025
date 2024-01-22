'''
Given a number N reverse the number and print it.

Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

Input Format

123

Constraints

N <= 1000

Output Format

321

Sample Input 0

123
Sample Output 0

321
Sample Input 1

2341
Sample Output 1

1432
'''

#code1
num =int(input())
rev_num = 0

while num != 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10

print(rev_num)

#code2
n=input()
print(n[::-1])
