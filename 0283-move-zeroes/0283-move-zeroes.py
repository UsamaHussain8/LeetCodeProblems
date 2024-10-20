class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums

        left = 0
        for right in range(left, len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1 
        
        return
        
