# Fractional Knapsack using Greedy Method
def fractional_knapsack(values, weights, capacity):
 # Calculate value-to-weight ratio and store index
 n = len(values)
 items = []
 for i in range(n):
    ratio = values[i] / weights[i]
 items.append((ratio, values[i], weights[i]))

 # Sort items by descending ratio
 items.sort(reverse=True, key=lambda x: x[0])
 total_value = 0
 fractions = [0] * n # To store fraction of each item taken
 for ratio, value, weight in items:
    if capacity >= weight:
 # Take whole item
        capacity -= weight
        total_value += value
        fractions[values.index(value)] = 1
    else:
    # Take fractional part of item
        fraction = capacity / weight
        total_value += value * fraction
        fractions[values.index(value)] = fraction
    break # Knapsack is full
 return total_value, fractions
# Driver code
if __name__ == "__main__":
 values = [60, 100, 120] # Values of items
 weights = [10, 20, 30] # Weights of items
 capacity = 50 # Maximum capacity of knapsack
 max_value, fractions_taken = fractional_knapsack(values, weights, capacity)
 print("Maximum Value in Knapsack:", max_value)
 print("Fractions of items taken:", fractions_taken)