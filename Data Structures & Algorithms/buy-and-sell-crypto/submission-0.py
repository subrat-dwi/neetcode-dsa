class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        buy_price = prices[0]
        profit = 0

        for i in range(m):
            if prices[i] <= buy_price:
                buy_price = prices[i]
            else:
                profit = max(prices[i] - buy_price, profit)

        return profit
            