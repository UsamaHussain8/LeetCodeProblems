class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_chars = {}
        magazine_chars = {}

        for char in ransomNote:
            if char in ransomNote_chars:
                ransomNote_chars[char] += 1
            else:
                ransomNote_chars[char] = 1                   

        for char in magazine:
            if char in magazine_chars:
                magazine_chars[char] += 1
            else:
                magazine_chars[char] = 1 
        
        for key in ransomNote_chars:
            if ransomNote_chars[key] > magazine_chars.get(key, 0):
                return False

        return True