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


