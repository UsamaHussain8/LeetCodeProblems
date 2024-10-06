class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fre = {}
        len_basket = 0
        left = 0

        for right in range(left, len(fruits)):
            fre[fruits[right]] = fre.get(fruits[right], 0) + 1
            while len(fre) > 2:
                fre[fruits[left]] -= 1
                if fre[fruits[left]] == 0:
                    del fre[fruits[left]]
                left += 1
            len_basket = max(len_basket, right - left + 1)

        return len_basket