class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j, len(nums2)):
                        if nums2[k] > nums2[j]:
                            next_greater_element = nums2[k] 
                            break
                        else:
                            next_greater_element = -1
                        
                
            ans.append(next_greater_element)

        return ans