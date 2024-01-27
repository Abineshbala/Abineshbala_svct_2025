'''
consider two points,p=(px,py)  andq=(qx,qy) . We consider the inversion or point reflection,r=(rx,ry) , of point p across point q to be a 180degree rotation of point p around q.
Given  n sets of points p and q, find r for each pair of points and print two space-separated integers denoting the respective values of rx and ry on a new line.
Sample Input

2
0 0 1 1
1 1 2 2
Sample Output

2 2
3 3
'''

def findPoint(px, py, qx, qy):
    # Write your code here
    rx=2*qx-px
    ry=2*qy-py
    return [rx,ry]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
