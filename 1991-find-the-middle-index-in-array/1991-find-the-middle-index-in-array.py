class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for idx in range(0, len(nums)):
            total -= nums[idx]
            if total == left_sum:
                return idx
            left_sum += nums[idx]
        
        return -1