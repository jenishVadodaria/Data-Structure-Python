""" Given an array of length N and an integer x, you need to find and return the
    last index of integer x present in the array. Return -1 if it is not present in the array.
    Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
    You should start traversing your array from 0, not from (N - 1).
    Do this recursively. Indexing in the array starts from 0. """

""" Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x """

# Output Format : last index or -1
# Constraints : 1 <= N <= 10^3

# Sample Input :
# 4
# 9 8 10 8
# 8
# Sample Output :
# 3


# SOLUTION :
def lastIndex(a, x):
    l = len(a)
    if l == 0:
        return -1
    smallerList = a[1:]
    smallerListOutput = lastIndex(smallerList, x)
    if smallerListOutput != -1:
        return smallerListOutput+1
    else:
        if a[0] == x:
            return 0
        else:
            return -1


def lastIndexB(a, x, si):
    l = len(a)
    if si == l:
        return -1
    smallerListOutput = lastIndexB(a, x, si+1)
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if a[si] == x:
            return si
        else:
            return -1


a = [1, 4, 5, 4, 8]
x = 4
print(lastIndex(a, x))
print(lastIndexB(a, x, 0))
