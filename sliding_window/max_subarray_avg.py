"""

- Given an integer array nums and an integer k

- Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

"""

def max_subarray_avg(nums, k):
    cur_sum = sum(nums[:k])
    max_sum = cur_sum

    for i in range(len(nums) - k):
        cur_sum += nums[i + k] - nums[i]
        max_sum = max(max_sum, cur_sum)
    
    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4

print(max_subarray_avg(nums, k))

# same as max subarray sum 

# time complexity: O(n)

# space complexity: O(1)

# since, k is constant, we don't need to find the average in every iteration, we can just find the maximum sum and then return the average at the end