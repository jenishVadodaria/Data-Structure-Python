def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)
    return


# PRINTS THE REVERSE of N Natural NUMBERS
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)


n = int(input())

print(print_1_to_n(n))
print(print_n_to_1(n))
