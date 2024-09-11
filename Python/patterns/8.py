# ========
#  =====
#   ===
#    =

n = 5
for i in range(n - 1, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")

    for j in range(2 * i + 1):
        print("*", end=" ")

    for j in range(n - i - 1):
        print(" ", end=" ")

    print()


# 0,7,0
# 1,5,5
# 2,3,2
# 3,1,3
