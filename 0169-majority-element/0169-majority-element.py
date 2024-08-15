class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        num = 0
        num_elements = len(nums)

        if num_elements == 1:
            return nums[0]
             
        for idx in range(0, num_elements):
            if nums[idx] in counter.keys():
                counter[nums[idx]] += 1
                if counter[nums[idx]] > num_elements // 2:
                    num = nums[idx]
            else:
                counter[nums[idx]] = 1    
            
        return num    