class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        num_elements = len(prices)
        buy_price = prices[0]
        
        for i in range(1, num_elements):
            #max_profit_one_time = max(prices[i] - buy_price, max_profit_one_time)
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit
