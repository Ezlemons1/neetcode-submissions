class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmax = 0
        i = 0
        j = i + 1
        while i < len(prices) - 1:
            tempmax = prices[j] - prices[i]

            if tempmax > currmax:
                currmax = tempmax
            
            if j == len(prices) - 1:
                i += 1
                j = i + 1
            else:
                j += 1
        
        return currmax