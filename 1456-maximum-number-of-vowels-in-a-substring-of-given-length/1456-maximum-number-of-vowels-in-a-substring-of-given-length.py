class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n_vowels = 0
        left = 0

        for right in range(left, len(s)):
            substr = s[left: right + k]
            n_vowels_cur = 0
            for elem in substr:
                if elem in ["a", "e", "i", "o", "u"]:
                    n_vowels_cur += 1
            n_vowels = max(n_vowels, n_vowels_cur)
            left += 1

        return n_vowels