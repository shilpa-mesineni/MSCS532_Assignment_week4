
#Partition
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    # Place the pivot element in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Test the partition function
if __name__ == "__main__":
    # Sample input array
    arr = [10, 80, 30, 90, 40, 50, 70]
    low = 0
    high = len(arr) - 1

    print("Original array:", arr)
    
    # Call partition
    partition_index = partition(arr, low, high)
    
    print("Array after partitioning:", arr)
    print("Pivot element index:", partition_index)
    print("Pivot element:", arr[partition_index])


# quicksort
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index
        quicksort(arr, low, pi - 1)     # Recursively sort the left subarray
        quicksort(arr, pi + 1, high)    # Recursively sort the right subarray

# Example to test the deterministic version
if __name__ == "__main__":
    arr = [10, 80, 30, 90, 40, 50, 70]
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array (Deterministic Quicksort):", arr)



import random

def randomized_partition(arr, low, high):
    # Generate a random index between low and high
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]  # Swap the pivot with the last element
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)  # Partitioning index
        randomized_quicksort(arr, low, pi - 1)     # Recursively sort left subarray
        randomized_quicksort(arr, pi + 1, high)    # Recursively sort right subarray

# Example to test the randomized version
if __name__ == "__main__":
    arr = [10, 80, 30, 90, 40, 50, 70]
    randomized_quicksort(arr, 0, len(arr) - 1)
    print("Sorted array (Randomized Quicksort):", arr)



'''
Performance Analysis (Time Complexity)
For deterministic Quicksort:
1. Best Case: O(nlogn),when the pivot divides the array into two equal parts.
2. Average Case: O(nlogn), due to random distribution of elements.
3. Worst Case: O(n2), when the pivot repeatedly divides the array into unbalanced parts (e.g., already sorted array).
For randomized Quicksort:
1. Best Case: O(nlogn).
2. Average Case: O(nlogn), since randomization reduces the probability of worst-case scenarios.
3. Worst Case: O(n2), but it is much less likely compared to deterministic Quicksort.
'''


import time

# Helper function to measure time taken by quicksort functions
def measure_time(func, arr):
    start_time = time.time()
    func(arr, 0, len(arr) - 1)
    return time.time() - start_time

if __name__ == "__main__":
    # Test arrays
    random_array = [random.randint(1, 1000) for _ in range(1000)]
    sorted_array = sorted(random_array)
    reverse_sorted_array = sorted(random_array, reverse=True)

    # Measure time for deterministic quicksort
    print("Deterministic Quicksort:")
    print("Random array:", measure_time(quicksort, random_array.copy()), "seconds")
    print("Sorted array:", measure_time(quicksort, sorted_array.copy()), "seconds")
    print("Reverse sorted array:", measure_time(quicksort, reverse_sorted_array.copy()), "seconds")

    # Measure time for randomized quicksort
    print("\nRandomized Quicksort:")
    print("Random array:", measure_time(randomized_quicksort, random_array.copy()), "seconds")
    print("Sorted array:", measure_time(randomized_quicksort, sorted_array.copy()), "seconds")
    print("Reverse sorted array:", measure_time(randomized_quicksort, reverse_sorted_array.copy()), "seconds")
