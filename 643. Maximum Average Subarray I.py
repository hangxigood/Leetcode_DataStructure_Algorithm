# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k 
        
        # first k number sum
        maximum = sum_num = sum(nums[0:k])
        # base the k size, the window move step from nums[1]
        for i in range(1,len(nums) - k + 1):
            # sum the numbers in the windows: just add new and remove old
            sum_num += nums[k+i-1]
            sum_num -= nums[i-1]
            # compare every window's sum
            maximum = max(maximum, sum_num)
        return maximum/k
