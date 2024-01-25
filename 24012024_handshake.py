'''
At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?
Example
n=3
There are 3 attendees,p1 , p2 and p3. p1 shakes hands with p2 and p3, and  shakes hands with p3. Now they have all shaken hands after 3 handshakes.

Sample Input

2
1
2
Sample Output

0
1
'''
def handshake(n):
    # Write your code here
    return n * (n - 1) // 2
test_cases=int(input())
for _ in range(test_cases):
    attendes=int(input())
    result=handshake(attendes)
    print(result)
