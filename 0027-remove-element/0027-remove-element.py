class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while (idx < len(nums)):
            if nums[idx] == val:
                nums.remove(val) 
            else:
                idx = idx + 1        
        return idx  