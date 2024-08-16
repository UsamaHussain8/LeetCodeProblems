class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_elements: int = len(nums)
        if num_elements <= 2:
            return num_elements

        j: int = 2
        for i in range(2, num_elements):            
            if nums[i] != nums[j - 2]:                
                nums[j] = nums[i]  
                j += 1
       
        return j