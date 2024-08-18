class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_elements = len(prices)
        if num_elements < 2:
            return 0
        
        # min_element: int = prices[0]
        # min_idx: int = 0

        # # for i in range(1, num_elements):
        # #     if prices[i] <= min_element:
        # #         min_element = prices[i]
        # #         min_idx = i 

        # left: int = 0
        # right: int = num_elements - 1
        # while left != right:
        #     if prices[left] <= prices[right]:
        #         min_element = min(prices[left], min_element)      
        #         left += 1
        #     else:
        #         min_element = min(prices[right], min_element)                
        #         right -= 1  

        # min_idx = prices.index(min_element)
        # if min_idx == num_elements - 1:
        #     return 0

        # profit = min_element

        # for i in range(min_idx + 1, num_elements):
        #     if profit < prices[i] - min_element:
        #         profit = prices[i] - min_element
            
        # return profit

        mid = num_elements // 2
        min_element = min(prices[0: mid + 1])
        min_idx = prices.index(min_element)
        max_element = max(prices[min_idx: num_elements])

        return max(max_element - min_element, 0)
            