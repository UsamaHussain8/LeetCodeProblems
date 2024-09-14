class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum: int = 0
        right_sum: int = 0

        for i in range(len(nums)):
            if i == 0:
                left_sum = right_sum = 0
                if sum(nums[i + 1: len(nums)]) == left_sum:
                    return i
            elif i == len(nums) - 1:
                left_sum = right_sum = 0
                if sum(nums[i - 1: 0: -1]) + nums[0] == right_sum:
                    return i
            else:
                left_sum = right_sum = 0
                left_sum = sum(nums[0: i])
                right_sum = sum(nums[i + 1: len(nums)])
                if left_sum == right_sum:
                    return i

        return -1