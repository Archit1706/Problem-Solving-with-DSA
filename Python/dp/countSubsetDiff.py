# Recursive code for count subset sum with given difference problem without memoization
# def countSubsetSumDiff(arr, diff, n):
#     summ = (sum(arr) + diff) // 2

#     def subsetSum(arr, sum, n):
#         if sum == 0:
#             return 1
#         if n == 0:
#             return 0

#         if arr[n - 1] <= sum:
#             return subsetSum(arr, sum - arr[n - 1], n - 1) + subsetSum(arr, sum, n - 1)

#         else:
#             return subsetSum(arr, sum, n - 1)

#     return subsetSum(arr, summ, n)

# recursive code for count of subsets sum with given difference with memoization using tabulation method
# def countSubsetSumDiff(arr, diff, n):
#     summ = (sum(arr) + diff) // 2
#     t = [[-1 for _ in range(summ + 1)] for _ in range(n + 1)]
#     def subsetSum(arr, sum, n):
#         if sum == 0:
#             return 1
#         if n == 0:
#             return 0

#         if arr[n - 1] <= sum:
#             t[n][sum] = subsetSum(arr, sum - arr[n - 1], n - 1) + subsetSum(arr, sum, n - 1)

#         else:
#             t[n][sum] = subsetSum(arr, sum, n - 1)

#         return t[n][sum]

#     return subsetSum(arr, summ, n)


# Iterative approach for count of subset sum with given difference with memoization using tabulation method (top-down approach)
def countSubsetSumDiff(arr, diff, n):
    summ = (sum(arr) + diff) // 2
    t = [[-1 for _ in range(summ + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(summ + 1):
            if i == 0:
                t[i][j] = 0

            if j == 0:
                t[i][j] = 1

    for i in range(1, n + 1):
        for j in range(1, summ + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]

            else:
                t[i][j] = t[i - 1][j]

    return t[n][summ] 


arr = [1, 2, 3, 1, 2]
n = 5
diff = 1
print(countSubsetSumDiff(arr, diff, n))
