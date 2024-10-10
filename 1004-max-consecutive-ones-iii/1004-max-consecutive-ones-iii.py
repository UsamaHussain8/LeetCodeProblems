class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_ones = num_zeros = 0
        left = 0

        for right in range(left, len(nums)):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            num_ones = max(num_ones, right - left + 1)

        return num_ones
