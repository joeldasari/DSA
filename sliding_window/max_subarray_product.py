"""
Problem: Maximum Product Subarray of Size K
Given an array of integers and an integer k, find the maximum product of any contiguous subarray of size exactly k.
Example:

Input: arr = [1, -2, -3, 0, 7, -8, -2], k = 3

Output: 112

Explanation: Subarray [7, -8, -2] has product 7 * (-8) * (-2) = 112.

"""

def max_subarray_product(arr, k): 
    max_prod = float("-inf")
    for i in range(len(arr) - k + 1):
        cur_prod = 1
        for j in range(i, i + k):
            cur_prod *= arr[j]
        max_prod = max(max_prod, cur_prod)
    return max_prod

arr = [1, -2, -3, 0, 7, -8, -2]
k = 3

print(max_subarray_product(arr, k))

# Time Complexity: O(nk)

# Space Complexity: O(1)