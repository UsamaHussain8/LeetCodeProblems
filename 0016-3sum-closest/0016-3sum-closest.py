class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        left: int = 0
        closest_sum: int = 99999
        nums.sort()

        for left in range(len(nums)):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            
            mid: int = left + 1
            right: int = len(nums) - 1   

            while mid < right:
                threeSum: int = nums[left] + nums[mid] + nums[right]
                if threeSum == target:
                    return threeSum

                if abs(threeSum - target) < abs(closest_sum - target):
                    closest_sum = threeSum


                if threeSum < target:
                    mid += 1
                else: 
                    right -= 1    

        return closest_sum 