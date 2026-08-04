class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        buy, sell = 0, 1
        currentMax = 0
        # if negative
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                currentMax = max(profit, currentMax)
            else:
                buy = sell
            sell += 1
        return currentMax
