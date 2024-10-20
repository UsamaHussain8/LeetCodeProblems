class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        num_operations = 0

        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum == k:
                num_operations += 1
                left += 1
                right -= 1
            elif cur_sum < k:
                left += 1
            else:
                right -= 1
            
        return num_operations