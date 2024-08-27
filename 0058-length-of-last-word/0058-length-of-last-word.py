class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i: int = len(s) - 1
        if i < 0:
            return 0

        while s[i] == ' ':
            i -= 1

        length_last_word: int = 0
        while s[i] != ' ' and i >= 0:
            length_last_word += 1
            i -= 1

        return length_last_word