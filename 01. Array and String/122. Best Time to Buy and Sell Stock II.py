class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cur = prices[0]
        ans = 0
        for price in prices:
            if price > cur:
                ans += price - cur
            cur = price
        return ans