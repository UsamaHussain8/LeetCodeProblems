class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_elements = len(prices)
        if num_elements < 2:
            return 0
        
        price_for_buying: int = prices[0]
        profit: int = 0
        
        for i in range(1, num_elements):
            if prices[i] < price_for_buying:
                price_for_buying = prices[i]
            profit = max(prices[i] - price_for_buying, profit)    
            
        return profit        