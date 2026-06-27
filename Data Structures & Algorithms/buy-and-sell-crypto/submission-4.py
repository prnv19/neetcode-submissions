class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                maxp = max(maxp, prices[r] - prices[l])
        
        return maxp
        
        