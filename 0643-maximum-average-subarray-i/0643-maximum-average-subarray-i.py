class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        len_nums: int = len(nums)
        if len_nums <= 1:
            return nums[0] / 1
        
        subarray_sums: int = [0] * (len_nums // 2)
        subarray_sums[0] = sum(nums[0: k])
        for left in range(1, len_nums // 2):
            right = left + k
            if right > len_nums:
                break
            subarray_sums[left] = subarray_sums[left - 1] + nums[right - 1] - nums[left - 1] 

        return max(subarray_sums) / k