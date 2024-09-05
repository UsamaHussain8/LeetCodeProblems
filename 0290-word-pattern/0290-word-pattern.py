class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words_list: List[str] = []
        len_s: int = len(s)
        len_pattern: int = len(pattern)
        start: int = 0
        for idx, char in enumerate(s):
            if char == ' ' and idx < len_s - 1:
                words_list.append(s[start: idx])
                start = idx + 1 
            elif idx == len_s - 1:
                words_list.append(s[start: len_s])

        if len_pattern != len(words_list):
            return False

        letter_word_mapper = {}
        for idx, char in enumerate(pattern):
            if char in letter_word_mapper.keys():
                if words_list[idx] != letter_word_mapper.get(char):
                    return False
            else:
                if words_list[idx] in list(letter_word_mapper.values()):
                    return False
            letter_word_mapper[char] = words_list[idx]
        
        return True