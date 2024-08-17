class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        num_elements = len(nums)
        if num_elements < 2 or k == num_elements:
            return

        num_times_to_rotate = k % num_elements
        times_rotated = 0
        temp_list = []
        for i in range(0, num_elements - k):
            temp_list.append(nums[i])
            
        del nums[0:num_elements - k]
        for j in range(0, len(temp_list)):
            nums.append(temp_list[j])
        
        return nums