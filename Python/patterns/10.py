# =
# ==
# ===
# ====
# ===
# ==
# =

n = 6
for i in range(n - 1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n - 1, -1, -1):
    for j in range(i):
        print("*", end=" ")
    print()
