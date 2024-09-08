class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length: int = len(nums)
        sorted_list = sorted(nums, reverse=True)

        left: int = 0
        for left in range(length):
            right: int = left
            while right < length:
                if sum(sorted_list[left: right + 1]) == target:
                    return len(sorted_list[left: right + 1])
                right += 1
                
        return 0