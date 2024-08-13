class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      if len(nums) == 0:
        return [-1, -1]

      indices = []

      left: int = 0
      right: int = len(nums) - 1
      
      while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                indices.append(mid)
                if (left + right <= 2) and (nums[mid - 1] != target or nums[mid + 1] != target):
                    indices.append(mid)    
                else:    
                    indices.insert(0, left) if (nums[left] == target and left != mid)  else indices.append(right)
                return indices

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1    

      if len(indices) == 0:
            return [-1, -1]