class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num: str = str(num)
        len_num: int = len(str_num)
        k_beauty: int = 0
        left: int = 0

        while left + k - 1 < len_num:
            right: int = left + k - 1
            sub_num: int = int(str_num[left: right + 1])
            if sub_num != 0 and num % sub_num == 0:
                k_beauty += 1

            left += 1

        return k_beauty