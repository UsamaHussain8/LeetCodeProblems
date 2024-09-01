class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_str: str = [char.lower() for char in s if char.isalnum()]
        alphanum_str = ''.join(alphanum_str)
        num_characters: int = len(alphanum_str)

        if num_characters == 0:    
            return True
        
        left: int = 0
        right: int = num_characters - 1
        while left <= num_characters // 2:
            if alphanum_str[left] != alphanum_str[right]:
                return False
            left += 1
            right -= 1

        return True