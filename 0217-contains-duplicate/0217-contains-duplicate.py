class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elem_freq = {}
        for num in nums:
            elem_freq[num] = elem_freq.get(num, 0) + 1
        
        for key in elem_freq.keys():
            if elem_freq[key] > 1:
                return True

        return False   