'''
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Function Description

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last names are each ≤ .

Sample Input 0

Ross
Taylor
Sample Output 0

Hello Ross Taylor! You just delved into python.
'''

def print_full_name(first, last):
    # Write your code here
    print("Hello "+first,last+"! You just delved into python.")
first_name=input()
last_name=input()
print_full_name(first_name,last_name)

#code2
def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first,last))
first_name=input()
last_name=input()
print_full_name(first_name,last_name)

