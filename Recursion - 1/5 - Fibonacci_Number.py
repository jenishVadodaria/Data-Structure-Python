def fib(n):
    if n == 1 or n == 2:
        return 1
    fib_n_1 = fib(n-1)
    fib_n_2 = fib(n-2)
    output = fib_n_1+fib_n_2
    return output


# Python 3 input() returns a string.To convert it to an integer, use int()
n = int(input("Enter a digit : "))
print(fib(n))
