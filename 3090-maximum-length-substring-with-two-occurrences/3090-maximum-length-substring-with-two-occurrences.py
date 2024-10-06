class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq_characters = {}
        len_sub = 0
        left = 0

        for right in range(left, len(s)):
            freq_characters[s[right]] = freq_characters.get(s[right], 0) + 1
            while freq_characters[s[right]] > 2:
                freq_characters[s[left]] -= 1
                left += 1
            len_sub = max(len_sub, right - left + 1)    
            
        return len_sub