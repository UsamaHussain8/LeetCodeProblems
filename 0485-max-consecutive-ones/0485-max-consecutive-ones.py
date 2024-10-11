class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_cons_ones = left = 0

        for right in range(left, len(nums)):
            if nums[right] == 1:
                num_cons_ones = max(num_cons_ones, right - left + 1)
            else:
                left = right + 1

        return num_cons_ones