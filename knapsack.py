# 0-1 Knapsack Problem using Dynamic Programming
def knapsack(values, weights, capacity):
 n = len(values)

 # Create DP table of size (n+1) x (capacity+1)
 dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

 # Build table dp[][] in bottom-up manner
 for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
 # Max of including or excluding the current item
            dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i -1][w])
        else:
            dp[i][w] = dp[i - 1][w]

 # To find which items are included
 w = capacity
 items_taken = []
 for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        items_taken.append(i - 1)
 w -= weights[i - 1]
 items_taken.reverse() # Optional: to show in order
 return dp[n][capacity], items_taken

# Driver code
if __name__ == "__main__":
    values = [60, 100, 120] # Values of items
    weights = [10, 20, 30] # Weights of items
    capacity = 50 # Maximum capacity of knapsack
    max_value, items_taken = knapsack(values, weights, capacity)
    print("Maximum Value in Knapsack:", max_value)
    print("Items taken (0-based indices):", items_taken)