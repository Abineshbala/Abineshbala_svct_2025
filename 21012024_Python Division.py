'''
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.

Input Format

The first line contains the first integer,a .
The second line contains the second integer,b .

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333
'''



a = int(input())
b = int(input())
int_div=a//b
print(int_div)
float_div=a/b
print(float_div)
