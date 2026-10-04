class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        m = prices[0]
        ans = 0
        for price in prices:
            ans = max(ans, price - m)
            m = min(m, price)
        return ans