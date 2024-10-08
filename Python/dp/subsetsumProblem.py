# Recursive SubSet Sum Problem Code w/o memoization
# def subsetsum(arr, sum, n):
#     if sum == 0:
#         return True

#     if n == 0:
#         return False

#     if arr[n - 1] <= sum:
#         return max(subsetsum(arr, sum - arr[n - 1], n - 1), subsetsum(arr, sum, n - 1))

#     else:
#         return subsetsum(arr, sum, n - 1)

arr = [1, 4, 2, 6, 5]
sum = 11
n = 5

# Recursive subset sum problem code with memoization
# t = [[None for _ in range(sum + 1)] for _ in range(n + 1)]


# def subsetsum(arr, sum, n):
#     if sum == 0:
#         return True

#     if n == 0:
#         return False

#     if t[n][sum] is not None:
#         return t[n][sum]

#     if arr[n - 1] <= sum:
#         t[n][sum] = subsetsum(arr, sum - arr[n - 1], n - 1) or subsetsum(
#             arr, sum, n - 1
#         )
#         return t[n][sum]

#     else:
#         t[n][sum] = subsetsum(arr, sum, n - 1)
#         return t[n][sum]


# iterative subset sum with memoization using a tabulation method (top-down-approach)
def subsetsum(arr, sum, n):
    t = [[None for _ in range(sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(sum + 1):
            if i == 0:
                t[i][j] = False

            if j == 0:
                t[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]

            else:
                t[i][j] = t[i - 1][j]

    return t[n][sum]


print(subsetsum(arr, sum, n))
