class Solution:
    def binarySearch(self, nums, target: int, left_present: bool):
        left: int = 0
        right: int = len(nums) - 1
        idx: int = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1                
            elif nums[mid] > target:
                right = mid - 1
            else:
                idx = mid    
                if left_present == True:
                    right = mid - 1
                else:
                    left = mid + 1    

        return idx            

    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1, -1]

        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)  

        return [left, right]