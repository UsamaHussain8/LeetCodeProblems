class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        currWindow, currLen, currVowelCount = [], 0, 0
        left = 0
        n = len(s)
        vowels = "AEIOUaeiou"
        ret = 0

        for right in range(n):
            letter = s[right]
            currWindow.append(letter)
            currLen += 1
            if letter in vowels:
                currVowelCount += 1
            
            while currLen > k:
                removedLetter = s[left]
                currWindow.remove(removedLetter)
                currLen -= 1
                if removedLetter in vowels:
                    currVowelCount -= 1
                left += 1
            
            # at this point satisfy the condition
            if currLen == k:
                ret = max(ret, currVowelCount)
        
        return ret