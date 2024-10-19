class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        num_subarrays = 0
        cur_sum = 0

        for right in range(left, len(nums)):
            cur_sum += nums[right]
            while cur_sum > k:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == k:
                num_subarrays += 1
                cur_sum = nums[right]
                left = right

        return num_subarrays