'''
Luke is daydreaming in Math class. He has a sheet of graph paper with  rows and  columns, and he imagines that there is an army base in each cell for a total of  bases. He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot. If a base contains at least one package inside or on top of its border fence, then it's considered to be supplied. For example:

image

Given  and , what's the minimum number of packages that Luke must drop to supply all of his bases?

Sample Input 0

2 2
Sample Output 0

1
'''


def gameWithCells(n, m):
    return ((n + 1) // 2) * ((m + 1) // 2)
rows=int(input())
column=int(input())

result = gameWithCells(rows, columns)
print(result)
