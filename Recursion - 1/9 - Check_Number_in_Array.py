""" Given an array of length N and an integer x, you need to find if x is present in the array or not.
    Return true or false. Do this recursively."""

"""Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x """

# Output Format : 'true' or 'false'
# Constraints : 1 <= N <= 10^3

# Sample Input 1 :
# 3
# 9 8 10
# 8
# Sample Output 1 :
# true
# Sample Input 2 :
# 3
# 9 8 10
# 2
# Sample Output 2 :
# false


# SOLUTION :




from sys import setrecursionlimit
def checkNumber(arr, x):
    return x in arr


# Main
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
