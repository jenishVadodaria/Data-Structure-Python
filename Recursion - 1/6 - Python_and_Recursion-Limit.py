import sys


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


def fact1(n):
    if n == 0:
        return 1
    smalloutput = fact(n-1)
    return n*smalloutput


# Sets the recursion call value as per the user instruction.
sys.setrecursionlimit(3000)

n = int(input("Enter a digit : "))
print(fact(n))
