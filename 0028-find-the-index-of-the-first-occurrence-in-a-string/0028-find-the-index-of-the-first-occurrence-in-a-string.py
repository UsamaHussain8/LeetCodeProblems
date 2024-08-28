class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length: int = len(needle)
        haystack_length: int = len(haystack)

        if needle_length > haystack_length or haystack_length == 0 or needle_length == 0:
            return -1

        j: int = 0
        starting_idx: int = -1
        while j in range(0, haystack_length):
            substring: str = haystack[j:j + needle_length]
            i: int = 0
            while i in range(0, needle_length):
                if substring[i] == needle[i]:
                    i += 1
                    if i == needle_length:
                        starting_idx = j
                        return starting_idx
                    elif j + needle_length > haystack_length:
                        return -1
                else:
                    j += 1
                    break

        return starting_idx