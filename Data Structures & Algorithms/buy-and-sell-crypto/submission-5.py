class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 0

        while sell < len(prices):
            if prices[sell] - prices[buy] < 0:
                buy = sell
            
            profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        return profit

        