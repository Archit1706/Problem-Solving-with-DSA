# print n to 1

n = 10

# def print_reverse_n(i):
#     if i < 1:
#         return

#     print(i)
#     print_reverse_n(i - 1)

# def main():
#     print_reverse_n(n)

# main()


def print_reverse(n):
    # Base Condition
    if n == 0:
        return

    # Induction
    print(n)

    # Hypothesis
    print_reverse(n - 1)


def main():
    print_reverse(n)


main()
