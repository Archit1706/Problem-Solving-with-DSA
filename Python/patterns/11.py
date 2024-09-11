n = 6
# for i in range(1, n):
#     for j in bin(i).split("b")[1]:
#         print(j, end=" ")
#     print()

for i in range(n):
    if i % 2 == 0:
        start = 1
    else:
        start = 0

    for j in range(i + 1):
        print(start, end=" ")
        start = 1 - start
    print()
