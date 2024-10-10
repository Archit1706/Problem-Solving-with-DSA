# # Recursive code for the minimum subset sum difference problem without memoization


# # # Recursive code for the minimum subset sum difference problem with memoization using tabulation
# # def minSubsetSumDiff(arr, n):
# #     sm = sum(arr)
# #     t = [[None for _ in range(sm + 1)] for _ in range(n + 1)]

# #     def subsetSum(arr, sum, n):
# #         if sum == 0:
# #             return True

# #         if n == 0:
# #             return False

# #         if arr[n - 1] <= sum:
# #             t[n][sum] = subsetSum(arr, sum - arr[n - 1], n - 1) or subsetSum(
# #                 arr, sum, n - 1
# #             )

# #         else:
# #             t[n][sum] = subsetSum(arr, sum, n - 1)

# #         return t[n][sum]

# #     res = subsetSum(arr, sm, n)
# #     print(t)
# #     # v = t[-1]
# #     # print(v)

# #     mn = 10**5
# #     # for i, n in enumerate(t):
# #     #     if n == True:
# #     #         mn = min(mn, sm - 2 * n)
# #     # return mn

# #     for i in range(n = 1):
# #         for j in range(sum + 1):
# #             if t[i][j] == True:
# #                 mn = min()


# # Iterative code for the minimum subset sum difference problem using tabulation method (top down approach)


# def minSubsetSumDiff(arr, n):
#     sm = sum(arr)

#     t = [[None for _ in range(sm + 1)] for _ in range(n + 1)]

#     def subsetSum(arr, sum, n):
#         for i in range(n + 1):
#             for j in range(sm + 1):
#                 if i == 0:
#                     t[i][j] = False

#                 if j == 0:
#                     t[i][j] = True

#         for i in range(1, n + 1):
#             for j in range(1, sm + 1):
#                 if arr[i - 1] <= j:
#                     t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]

#                 else:
#                     t[i][j] = t[i - 1][j]

#     subsetSum(arr=arr, sum=sm // 2, n=n)

#     print(t)
#     v = t[-1]
#     print(v)

#     mn = 10**5
#     for i in range(len(v)):
#         if i <= sm // 2 and v[i] == True:
#             mn = min(mn, sm - 2 * i)

#     return mn


def minimumDifference(nums):
    def subsetSum(arr, sum, n):
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

        return t

    trange = sum(nums)

    t = subsetSum(arr=nums, sum=trange // 2, n=len(nums))
    print(t)

    v = t[-1]
    print(v)

    mn = 10**9
    for i in range(len(v)):
        if v[i] == True:
            mn = min(mn, trange - 2 * i)

    return mn


arr = [1, 6, 11, 5]
n = 4
print(minimumDifference(arr))
# print(minSubsetSumDiff(arr, n))
