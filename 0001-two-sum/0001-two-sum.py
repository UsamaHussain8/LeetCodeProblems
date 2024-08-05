class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_indices_map = {}
        for i, num in enumerate(nums):
          complement = target - num
          if complement in required_indices_map:
            return [required_indices_map[complement], i]
          required_indices_map[num] = i
        
        return []