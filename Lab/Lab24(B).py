# 0/1 Knapsack using Dynamic Programming

def knapsack(W, wt, val, n):
    # Create DP table
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Values and Weights
value = [60, 100, 120]
weight = [10, 20, 30]

capacity = 50
n = len(value)

print("Maximum Profit =", knapsack(capacity, weight, value, n))
