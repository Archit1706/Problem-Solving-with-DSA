#    *
#   ***
#  *****
# *******

n = 4
for i in range(n):
    # print spaces
    for s in range(n - i - 1):
        print(" ", end=" ")
    for _ in range(2 * i + 1):
        print("*", end=" ")
    for _ in range(n - i - 1):
        print(" ", end=" ")
    print()

# n = 4
#    =
#   ===
#  =====
# =======

# [3, 1, 3]
# [2, 3, 2]
# [1, 5, 1]
# [0, 7, 0]
