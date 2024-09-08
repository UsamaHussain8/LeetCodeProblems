class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_nums: int = len(nums)
        left = total = 0
        res = float("inf")
        
        for right in range(len_nums):
            total += nums[right]
            while total >= target:
                total -= nums[left]
                res = min(res, right - left + 1)
                left += 1

        return 0 if res == float("inf") else res