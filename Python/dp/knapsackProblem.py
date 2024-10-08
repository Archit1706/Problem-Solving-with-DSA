# # Recursive Knapsack Code w/o memoization
# def knapsack(wt, val, w, n):
#     if n == 0 or w == 0:
#         return 0

#     if wt[n - 1] <= w:
#         return max(val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1), knapsack(wt, val, w, n - 1))

#     else:
#         return knapsack(wt, val, w, n - 1)

# # Recursive knapsack code with memoization
# def knapsack(wt, val, w, n):
#     t = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]
#     if n == 0 or w == 0:
#         return 0

#     if t[n][w] != -1:
#         return t[n][w]

#     elif wt[n - 1] <= w:
#         t[n][w] = max(val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1), knapsack(wt, val, w, n - 1))
#         return t[n][w]

#     else:
#         t[n][w] = knapsack(wt, val, w, n - 1)
#         return t[n][w]


# Top Down Approach Knapsack Code
def knapsack(wt, val, w, n):
    t = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]

    # when n = 0 ie no item then the val is 0 and when the w = 0 ie we cannot put any item in the knapsack so the val is still 0
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

        # choice diagram
    for i in range(n + 1):
        for j in range(w + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])

            else:
                t[i][j] = t[i - 1][j]

    return t[n][w]


wt = [1, 3, 5, 4, 7]
val = [10, 20, 25, 15, 30]
w = 12
n = 5

print(knapsack(wt, val, w, n))
