class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count: int = 0
        left: int = 0
        len_s: int = len(s)

        for left in range(0, len_s - 2):
            right: int = left + 2
            if len(set(s[left : right + 1])) == 3:
                count += 1

        return count

             
