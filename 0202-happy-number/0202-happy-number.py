import time

class Solution:
    def isHappy(self, n: int) -> bool:
        timeout = time.time() + 0.001180 

        while n != 1:        
            if time.time() > timeout:
                return False
                
            componentDigits = self.findComponentDigits(n)
            n = sum([componentDigits[i] * componentDigits[i] for i in range(0, len(componentDigits))])
        
        return True

    def findComponentDigits(self, n: int):
        componentDigits = [int(digit) for digit in str(n)]

        return componentDigits