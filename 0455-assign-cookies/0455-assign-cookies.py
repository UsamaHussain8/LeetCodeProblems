class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_sorted = sorted(g)
        s_sorted = sorted(s)

        left_start = 0
        right_start = 0
        satisfied = 0

        while left_start < len(g_sorted) and right_start < len(s_sorted):
            if s_sorted[right_start] == g_sorted[left_start]:
                satisfied += 1
                left_start += 1
                right_start += 1
            elif s_sorted[right_start] > g_sorted[left_start]:
                left_start += 1
            else:
                right_start += 1
        
        return satisfied