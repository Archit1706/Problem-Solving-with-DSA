arr = [13, 9, 52, 46, 7, 89, 12]
n = len(arr)


def bubble_sort(arr, n):
    for i in range(n-1, -1, -1):
        print(i)
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
        print(arr)

    return arr


print(bubble_sort(arr, n))


# 13, 9, 52, 46, 7, 89, 12

# iteration 1

# |
# 13, 9, 52, 46, 7, 89, 12

# swap 9 and 13

# 9, 13, 52, 46, 7, 89, 12

# iteration 2

#     |
# 9, 13, 52, 46, 7, 89, 12

# iteration 3
#         |
# 9, 13, 52, 46, 7, 89, 12

# iteration 4
#             |
# 9, 13, 52, 46, 7, 89, 12

# swap 46 and 52

# 9, 13, 46, 52, 7, 89, 12

# iteration 5
#                |
# 9, 13, 46, 52, 7, 89, 12

# swap 7 and 52

# 9, 13, 46, 7, 52, 89, 12

# swap 46 and 7

# 9, 13, 7, 46, 52, 89, 12

# swap 7 and 13

# 9, 7, 13, 46, 52, 89, 12

# swap 7 and 9

# 7, 9, 13, 46, 52, 89, 12

# iteration 6
#                    |
# 7, 9, 13, 46, 52, 89, 12

# iteration 7
#                        |
# 7, 9, 13, 46, 52, 89, 12

# swap 12 and 89

# 7, 9, 13, 46, 52, 12, 89

# swap 12 and 52

# 7, 9, 13, 46, 12, 52, 89

# swap 12 and 46

# 7, 9, 13, 12, 46, 52, 89

# swap 12 and 13

# 7, 9, 12, 13, 46, 52, 89
