class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_elements = len(nums)
        ans: int = 0

        for i in range(0, num_elements):
            ans ^= nums[i]

        return ans