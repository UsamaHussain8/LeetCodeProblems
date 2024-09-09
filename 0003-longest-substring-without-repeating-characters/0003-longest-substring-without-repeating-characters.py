class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s: int = len(s)
        if len_s == 0:
            return 0

        left: int = 0        
        freq_characters = {}
        substr_count = {}
        count: int = 0

        for right in range(0, len_s):
            freq_characters[s[right]] = freq_characters.get(s[right], 0) + 1
            while freq_characters[s[right]] > 1:
                freq_characters[s[left]] -= 1
                left += 1

            count = max(count, right - left + 1)  
              
        return count