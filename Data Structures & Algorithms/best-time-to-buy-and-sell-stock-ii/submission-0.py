class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        profit = 0
        total_profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            if price > prices[i - 1]:
                profit = price - prices[buy_idx]
            else:
                total_profit += profit
                profit = 0
                buy_idx = i
        
        total_profit += profit
        return total_profit


                
