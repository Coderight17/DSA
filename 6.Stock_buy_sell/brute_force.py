class Solution:
    def maxProfit(self, prices) -> int:
        max = 0
        for i in range(len(prices)-1):
            bp = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > max:
                    max = prices[j] - prices[i]
        return max

prices = [7,1,5,3,6,4]
s = Solution()
max_profit = s.maxProfit(prices)
print(max_profit)
