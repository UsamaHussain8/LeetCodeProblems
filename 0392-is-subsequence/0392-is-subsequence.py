class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i: int = 0
        j: int = 0
        len_substr: int = len(s)
        len_str: int = len(t)

        while i < len_substr and j < len_str:
            if s[i] == t[j]:
                i += 1
            j += 1
            if j > len_str:
                return False

        if i == len_substr:
            return True
        else:
            return False