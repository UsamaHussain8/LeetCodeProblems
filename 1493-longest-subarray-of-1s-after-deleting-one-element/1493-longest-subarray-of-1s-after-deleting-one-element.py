class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_zeros = 0
        num_ones = 0
        left = 0

        for right in range(left, len(nums)):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros > 1:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
                
            num_ones = max(num_ones, right - left)
                    
        return num_ones

            
                