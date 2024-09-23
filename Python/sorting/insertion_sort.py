# 13 46 24 52 20 9

# iteration 1

# -> 13 is at its correct position
# |
# 13 46 24 52 20 9

# iteration 2
# -> 46 is at its correct position
#     |
# 13 46 24 52 20 9

# iteration 3
# -> 24 is not at its correct position
#       |
# 13 46 24 52 20 9

# swap 24 and 46

# 13 24 46 52 20 9

# iteration 3
#          |
# 13 24 46 52 20 9
# -> 52 is at its correct position

# iteration 4
#              |
# 13 24 46 52 20 9
# -> 20 is not at its correct position

# swap 20 and 52

# 13 24 46 20 52 9

# swap 20 and 46

# 13 24 20 46 52 9

# swap 20 and 24

# 13 20 24 46 52 9

# iteration 5

# 13 20 24 46 52 9

# 9 is not at its correct position

# swap 9 a nd 52

# 13 20 24 46 9 52

# swap 9 and 46
# 13 20 24 9 46 52

# swap 9 and 24

# 13 20 9 24 46 52

# swap 9 and 20

# 13 9 20 24 46 52

# swap 9 and 13

# 9 13 20 24 46 52

arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

for i in range(n):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        temp = arr[j-1]
        arr[j-1] = arr[j]
        arr[j] = temp
        j -= 1
    print(i)
    print(arr)

print(arr)
    