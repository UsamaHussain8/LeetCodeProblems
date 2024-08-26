class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_mapping = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        equivalent_number: int = 0

        for cur_idx in range(0, len(s)):
            char = s[cur_idx]
            next_idx = cur_idx + 1 if cur_idx + 1 < len(s) else cur_idx
            next_char = s[next_idx]

            if roman_to_int_mapping[char] < roman_to_int_mapping[next_char]:
                equivalent_number -= roman_to_int_mapping[char]
            else:
                equivalent_number += roman_to_int_mapping[char]

        return equivalent_number   