import random
import time

# ---------- DETERMINISTIC QUICK SORT ----------
def deterministic_partition(arr, low, high):
 pivot = arr[high]
 i = low - 1
 for j in range(low, high):
    if arr[j] <= pivot:
        i += 1
 arr[i], arr[j] = arr[j], arr[i]
 arr[i + 1], arr[high] = arr[high], arr[i + 1]
 return i + 1
def deterministic_quick_sort(arr, low, high):
 if low < high:
    pi = deterministic_partition(arr, low, high)
    deterministic_quick_sort(arr, low, pi - 1)
    deterministic_quick_sort(arr, pi + 1, high)

# ---------- RANDOMIZED QUICK SORT ----------
def randomized_partition(arr, low, high):
 rand_pivot = random.randint(low, high)
 arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
 return deterministic_partition(arr, low, high)
def randomized_quick_sort(arr, low, high):
 if low < high:
    pi = randomized_partition(arr, low, high)
    randomized_quick_sort(arr, low, pi - 1)
    randomized_quick_sort(arr, pi + 1, high)
    
# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
 size = int(input("Enter number of elements: "))
 arr = [random.randint(1, 1000) for _ in range(size)]
 # Make copies of the same array
 arr1 = arr.copy()
 arr2 = arr.copy()
 print("\nOriginal Array:", arr)
 # Deterministic Quick Sort
 start = time.time()
 deterministic_quick_sort(arr1, 0, len(arr1) - 1)
 end = time.time()
 print("\nSorted Array (Deterministic):", arr1)
 print("Time taken (Deterministic): {:.6f} seconds".format(end - start))
 # Randomized Quick Sort
 start = time.time()
 randomized_quick_sort(arr2, 0, len(arr2) - 1)
 end = time.time()
 print("\nSorted Array (Randomized):", arr2)
 print("Time taken (Randomized): {:.6f} seconds".format(end - start))