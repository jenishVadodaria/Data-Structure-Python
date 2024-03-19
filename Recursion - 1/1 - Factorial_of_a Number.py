# FACTORIAL OF A NUMBER

# METHOD - 1
def fact(n):
    if n == 0:                  # BASE CASE
        return 1
    return n*fact(n-1)          # RECURSION STEP


# METHOD - 2
def fact1(n):
    if n == 0:                  # BASE CASE
        return 1
    smalloutput = fact(n-1)     # RECURSION STEP
    return n*smalloutput


n = int(input("Enter a digit : "))
print(fact(n))
print(fact1(n))
