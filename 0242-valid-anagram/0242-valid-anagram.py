class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_counter_s = {}
        if len(s) != len(t):
            return False

        for char in s:
            freq_counter_s[char] = freq_counter_s.get(char, 0) + 1
        for char in t:
            if char not in freq_counter_s.keys() or freq_counter_s.get(char, 0) == 0:
                return False
            freq_counter_s[char] = freq_counter_s.get(char, 0) - 1    

        return True