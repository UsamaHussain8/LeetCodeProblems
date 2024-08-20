class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num_elements = len(nums)
        for i in range(0, num_elements):
            if i + nums[i] == num_elements - 1:
                return True

        return False        