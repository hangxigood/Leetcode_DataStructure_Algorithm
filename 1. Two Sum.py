# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:     
        for n in nums:
            test = nums.copy()
            test.remove(n)
            if n in test and 2*n == target:
                return [self.find_indices(nums, n), self.find_indices(test, n) + 1]
            elif target - n in test:
                return [self.find_indices(nums, n), self.find_indices(nums, target - n)]
            
    def find_indices(self, nums: list[int], target: int) -> int:
        i = 0
        for n in nums:
            if n == target:
                return i
            i += 1