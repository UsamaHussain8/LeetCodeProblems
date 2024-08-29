class Solution:
    def reverseWords(self, s: str) -> str:
        i: int = len(s) - 1
        reversed_string: str = ""
        while i > 0:
            left: int = i
            right: int = i

            while s[left] == ' ':
                left -= 1
            right = left

            while left >= 0 and s[left] != ' ':
                left -= 1

            reversed_string += s[left + 1: right + 1] + ' '
            right = left

            i = left

        return reversed_string.rstrip()