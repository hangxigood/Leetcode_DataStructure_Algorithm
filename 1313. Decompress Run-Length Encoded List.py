class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        i = 0 
        result = []

        while i < len(nums) // 2:
            freq = nums[2*i]
            val = nums[2*i+1]
            i += 1

            for _ in range(freq):
                result.append(val)
        
        return result 