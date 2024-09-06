class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_counter_t = {}
        freq_counter_s = {}
        if len(s) != len(t):
            return False

        for char in t:
            freq_counter_t[char] = freq_counter_t.get(char, 0) + 1
        for char in s:
            freq_counter_s[char] = freq_counter_s.get(char, 0) + 1

        return freq_counter_t == freq_counter_s