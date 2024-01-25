'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
Sample Input

chris alan
Sample Output

Chris Alan
'''
def solve(s):
    result = ' '.join(word.capitalize() for word in s.split())
    return result
input_string = input("Enter a string: ")
result =solve(input_string)
print("Capitalized String:", result)

