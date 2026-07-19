class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = sell = i
            else:
                sell = i
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
        
        return max_profit

        