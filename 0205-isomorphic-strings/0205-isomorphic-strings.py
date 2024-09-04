class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        char_mapper = {}

        if len_s > len_t:
            return False

        for i in range(0, len_s):
            if s[i] in char_mapper.keys() or t[i] in list(char_mapper.values()):
                if char_mapper.get(s[i]) != t[i]:
                    return False
            else:
                char_mapper[s[i]] = t[i]

        return True