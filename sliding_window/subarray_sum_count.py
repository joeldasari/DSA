"""
Problem: Count Subarrays with Sum Equal to Target of Size K
Given an array of integers, an integer k, and a target value, find the count of subarrays of size exactly k whose sum equals the target.
Example:

Input: arr = [1, 2, 3, 2, 4, 2, 5], k = 3, target = 6

Output: 2

Explanation: Subarrays of size 3 with sum 6:

[1, 2, 3] → sum = 6 ✓
[2, 2, 2] — doesn't exist here
[2, 4, 2] — sum = 8 ✗
Actually: [1,2,3] = 6 ✓ and [2,3,2] = 7 ✗ and [3,2,4] = 9 ✗ and [2,4,2] = 8 ✗ and [4,2,5] = 11 ✗

"""

# def subarray_sum_count(arr, k, target):
#     count = 0
#     for i in range(len(arr) - k + 1):
#         total = 0
#         for j in range(i, i + k):  
#             total += arr[j]
#         if target == total:
#             count += 1
#     return count

# Time Complexity: O(nk)
# Space Complexity: O(1)


# Optimized version

def subarray_sum_count(arr, k, target):
    count = 0
    cur_sum = sum(arr[:k])
    if cur_sum == target:
        count += 1
    for i in range(len(arr) - k):
        cur_sum += arr[i+k] - arr[i]
        if cur_sum == target:
            count += 1
    return count

# Time Complexity: O(n)
# Space Complexity: O(1)


arr = [1, 2, 3, 2, 4, 0, 2]
k = 3
target = 6

print(subarray_sum_count(arr, k, target))