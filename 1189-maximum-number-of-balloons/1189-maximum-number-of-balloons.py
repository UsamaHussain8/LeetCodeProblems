class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7:
            return 0

        freq_count = {}
        for char in text:
            if char in ['b', 'a', 'l', 'o', 'n']:
                freq_count[char] = freq_count.get(char, 0) + 1
        
        min_balloons = 1000000
       
        for char in 'balon':
            if char in ['b', 'a', 'n']:
                min_balloons = min(min_balloons, freq_count.get(char, 0)) 
                if min_balloons == 0:
                    return min_balloons
            else:
                min_balloons = min(min_balloons, freq_count.get(char, 0) // 2)
                if min_balloons == 0:
                    return min_balloons

        return min_balloons