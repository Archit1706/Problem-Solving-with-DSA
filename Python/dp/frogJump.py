def frogJump(height, n):
    # Code here
    # i = 0
    # energy = 0
    # while i < len(nums) - 1:
    #     if abs(height[i] - height[i + 1]) < abs(height[i] - height[i + 2]):
    #         min_energy = abs(height[i] - height[i + 1])
    #         i += 1
    #     else:
    #         min_energy = abs(height[i] - height[i + 2])
    #         i += 2
    #     energy += min_energy

    # return energy

    dp = [-1] * (n + 1)

    def helper(i):

        if i == 0:
            return 0

        if dp[i] != -1:
            return dp[i]

        else:
            c1 = helper(i - 1) + abs(heights[i] - heights[i - 1])

            c2 = 10**9
            if i > 1:
                c2 = helper(i - 2) + abs(heights[i] - heights[i - 2])

            dp[i] = min(c1, c2)
            return dp[i]

    return helper(n - 1)


height = [10, 20, 30, 10]
n = 4
print(frogJump(height, n))