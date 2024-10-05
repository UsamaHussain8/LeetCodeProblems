class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
            
        left = 0
        len_sub = 1
        right = left + 1
        
        while right < len(s):
            substr = s[left: right]
            for char in substr:
                if s[right] == char:
                    len_sub = max(len_sub, right - left)
                    left = right
            right += 1

        return len_sub
         