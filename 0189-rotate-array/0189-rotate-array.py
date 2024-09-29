class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_times_to_rotate = k % len(nums)
        if num_times_to_rotate == 0:
            return

        left, right = 0, len(nums) - 1
        self.reverse(nums, left, right)
        
        left, right = 0, num_times_to_rotate - 1
        self.reverse(nums, left, right)

        left, right = num_times_to_rotate, len(nums) - 1
        self.reverse(nums, left, right)
            
    def reverse(self, nums: List[int], left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1