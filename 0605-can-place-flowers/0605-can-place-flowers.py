class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i in range(len(flowerbed)):
            if n == 0:
                return True
            if i == 0 and flowerbed[i + 1] == 0 and flowerbed[i] != 1:
                flowerbed[i] = 1
                n -= 1
            elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0 and flowerbed[i] != 1:
                flowerbed[i] = 1 
                n -= 1
                if n == 0:
                    return True        
            elif flowerbed[i] == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1 and i != len(flowerbed) - 1:
                flowerbed[i] = 1
                n -= 1
            i += 1
                    
        return False