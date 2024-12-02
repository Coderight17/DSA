class Solution:
    def maxProfit(self, prices) -> int:
        min = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i-1]<min:
                min = prices[i-1]
            if prices[i]-min > profit:
                profit = prices[i]-min
        return profit
prices = [7,1,5,3,6,4]
s = Solution()
max_profit = s.maxProfit(prices)
print(max_profit)
