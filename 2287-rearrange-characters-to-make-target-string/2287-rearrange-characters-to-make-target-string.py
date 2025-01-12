class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if len(s) < len(target):
            return 0

        freq_count_s = {}
        for char in s:
            freq_count_s[char] = freq_count_s.get(char, 0) + 1
        freq_count_target = {}
        for char in target:
            freq_count_target[char] = freq_count_target.get(char, 0) + 1
        
        min_copies = 1000000
       
        for char in target:
            min_copies = min(min_copies, freq_count_s.get(char, 0)//freq_count_target.get(char, 0)) 
            if min_copies == 0:
                return min_copies
            # else:
            #     min_copies = min(min_copies, freq_count.get(char, 0) // 2)
            #     if min_copies == 0:
            #         return min_copies

        return min_copies