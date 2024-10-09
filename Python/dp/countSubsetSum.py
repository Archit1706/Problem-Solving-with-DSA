# recursive method for the count sub set sum problem without memoization
# def countSubSetSum(arr, sum, n):
#     if sum == 0:
#         return 1
#     if n == 0:
#         return 0

#     if arr[n - 1] <= sum:
#         return countSubSetSum(arr, sum - arr[n - 1], n - 1) + countSubSetSum(
#             arr, sum, n - 1
#         )

#     else:
#         return countSubSetSum(arr, sum, n - 1)


def countSubSetSum(arr, sum, n):
    t = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]

    if sum == 0:
        return 1

    if n == 0:
        return 0

    if t[n][sum] != -1:
        return t[n][sum]

    elif arr[n - 1] <= sum:
        t[n][sum] = countSubSetSum(arr, sum - arr[n - 1], n - 1) + countSubSetSum(
            arr, sum, n - 1
        )
        return t[n][sum]
    else:
        t[n][sum] = countSubSetSum(arr, sum, n - 1)

    return t[n][sum]


# Iterative approach for the count subset sum problem using tablualtion (top down approach)
# def countSubSetSum(arr, sum, n):
#     t = [[None for _ in range(sum + 1)] for _ in range(n + 1)]

#     for i in range(n + 1):
#         for j in range(sum + 1):
#             if i == 0:
#                 t[i][j] = 0

#             if j == 0:
#                 t[i][j] = 1

#     for i in range(1, n + 1):
#         for j in range(1, sum + 1):
#             if arr[i - 1] <= j:
#                 t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]

#             else:
#                 t[i][j] = t[i - 1][j]

#     return t[n][sum]


arr = [2, 3, 5, 8, 10]
n = 5
sum = 10

print(countSubSetSum(arr, sum, n))
