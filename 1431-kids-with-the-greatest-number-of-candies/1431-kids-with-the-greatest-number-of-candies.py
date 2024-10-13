class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if len(candies) == 0:
            return [False]

        max_candies = candies[0]
        for candy in range(len(candies)):
            if candies[candy] > max_candies:
                max_candies = candies[candy]

        greatest_candies = [False] * len(candies)
        for candy in range(len(candies)):
            if candies[candy] + extraCandies >= max_candies:
                greatest_candies[candy] = True

        return greatest_candies
