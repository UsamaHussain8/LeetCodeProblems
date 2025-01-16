class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        left = 0
        right = len(str_num) - 1


        while left <= right:
            if str_num[left] != str_num[right]:
                return False
            left += 1
            right -= 1

        return True