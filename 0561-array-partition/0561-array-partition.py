class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        max_sum = 0
        # after sorting it becomes really easy, we just need to sum elements at a step distance of 2 from each other
        for i in range(0, len(nums_sorted), 2):
            max_sum += nums_sorted[i]

        return max_sum