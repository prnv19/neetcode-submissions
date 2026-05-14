class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        max_profit = 0
        while s < len(prices):
            net = prices[s] - prices[b]
            if net < 0:
                b += 1
                if b == s:
                    s += 1
            else:
                max_profit = max(net, max_profit)
                s += 1
        return max_profit