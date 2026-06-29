class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for l in range(len(prices)):
            r = l + 1
            while r < len(prices) and prices[r] > prices[l]:
                maxProfit = max(maxProfit,prices[r] - prices[l])
                r += 1
        
        return maxProfit
        
            