# recursive code for partition equal subset problem without memoization


# def partitionEqualSubset(arr, n):
#     def subsetSum(arr, sum, n):
#         if n == 0:
#             return False

#         if sum == 0:
#             return True

#         if arr[n - 1] <= sum:
#             return max(
#                 subsetSum(arr, sum - arr[n - 1], n - 1), subsetSum(arr, sum, n - 1)
#             )

#         else:
#             return subsetSum(arr, sum, n - 1)

#     total = sum(arr)
#     if total % 2 != 0:
#         return False

#     else:
#         return subsetSum(arr=arr, sum=total // 2, n=n)


# Recursive code for partition equal subset problem with memoization
# def partitionEqualSubSet(arr, n):
#     t = [[None for _ in range(sum(arr) // 2 + 1)] for _ in range(n + 1)]

#     def subset(arr, sum, n, t):
#         if n == 0:
#             return False

#         if sum == 0:
#             return True

#         if arr[n - 1] <= sum:
#             t[n][sum] = max(
#                 subset(arr, sum - arr[n - 1], n - 1, t), subset(arr, sum, n - 1, t)
#             )
#             return t[n][sum]

#         else:
#             t[n][sum] = subset(arr, sum, n - 1, t)
#             return t[n][sum]

#     total = sum(arr)
#     if total % 2 != 0:
#         return False

#     else:
#         return subset(arr, total // 2, n, t)


# iterative code for partition equal subset problem with memoization using tabulation method (top-down approach)

def partitionEqualSubSet(arr, n):
    total = sum(arr)
    if total % 2 != 0:
        return False
    
    t = [[None for _ in range(total // 2 + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(total // 2 + 1):
            if i == 0:
                return False
            if j == 0:
                return True
            
    half = total // 2
            
    for i in range(n + 1):
        for j in range(half + 1):
            # if t[i][j] is not None:
            #     return t[i][j]
            
            if arr[i - 1] < j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            
            else:
                t[i][j] = t[i - 1][j]

    return t[n][sum]
                


arr = [1, 5, 11, 5]
n = 4

print(partitionEqualSubSet(arr, n))
