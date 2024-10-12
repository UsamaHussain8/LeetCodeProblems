class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = right = 0
        merged_string = ""

        while left < len(word1) and right < len(word2):
            merged_string += word1[left]
            merged_string += word2[right]
            left += 1
            right += 1

        if left < len(word1):
            while left < len(word1):
                merged_string += word1[left]
                left += 1

        if right < len(word2):
            while right < len(word2):
                merged_string += word2[right]
                right += 1

        return merged_string