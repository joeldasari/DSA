def max_subarray(arr, k):
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for i in range(len(arr) - k):
        current_sum += arr[i + k] - arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum


arr = [2, 1, 5, 1, 3, 2]

k = 3

print(max_subarray(arr, k))

# the sliding window size is fixed

# so, instead of calculating the sum for every window (using another loop to calculate the sum) we can just add the new number entering the window and subtract the previous number exiting the window

# time complexity: O(n)
# sum(arr[:k]) - time complexity is O(k), and overall we take O(n) time complexity

# space complexity: O(1) - only a few single-value variables used (no data structures ex: list, dict, etc.)

