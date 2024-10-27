class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discounts = [price for price in prices]
        stack = []

        for item, price in enumerate(prices):
            while stack and price <= stack[-1][1]:
                prev_item, prev_price = stack.pop()
                discounts[prev_item] = discounts[prev_item] - price
            stack.append([item, price])

        return discounts