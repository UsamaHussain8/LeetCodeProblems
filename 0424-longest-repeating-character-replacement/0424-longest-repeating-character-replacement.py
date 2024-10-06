class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        len_sub = 0
        fre_letters = {}
        left = 0

        for right in range(len(s)):
            fre_letters[s[right]] = fre_letters.get(s[right], 0) + 1
            if (right - left + 1) - max(fre_letters.values()) > k:
                fre_letters[s[left]] -= 1
                left += 1
            
            len_sub = max(len_sub, right - left + 1)
        
        return len_sub
