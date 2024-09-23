# print linearly from 1 to N

n = 10

# def print_n(i):
#     if i > n:
#         return

#     print(i)
#     print_n(i + 1)

# def main():
#     print_n(1)

# main()


def print_n(n):
    # Base Condition
    if n == 0:
        return

    # Hypothesis
    print_n(n - 1)

    # Induction
    print(n)


def main():
    print_n(n)


main()
