class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmax = 0
        tempmin = prices[0]
        for price in prices:
            currmax = max(currmax, price - tempmin)
            tempmin = min(tempmin, price)
        return currmax