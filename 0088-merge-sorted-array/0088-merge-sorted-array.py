class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = (nums2[i])

        pos = m + n - 1
        while n > 0 and m > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[pos] = nums2[n - 1]
                n -= 1
            else:
                nums1[pos] = nums1[m - 1]
                m -= 1
            pos -= 1

        while n > 0:
            nums1[pos] = nums2[n - 1]
            n -= 1
            pos -= 1