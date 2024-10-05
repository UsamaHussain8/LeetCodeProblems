class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
            
        left = 0
        len_sub = 0
        right = 0
        substr = set()
        
        while right < len(s):
            while s[right] in substr:
                substr.remove(s[left])
                left += 1

            substr.add(s[right])
            len_sub = max(len_sub, right - left + 1)
            right += 1

        return len_sub
         