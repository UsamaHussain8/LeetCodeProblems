class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discounts = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discounts.append(prices[i] - prices[j])
                    break
                if j == len(prices) - 1:
                    discounts.append(prices[i])
            if i == len(prices) - 1:
                discounts.append(prices[i])

        return discounts