class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        ans= 0
        for high in range(1,n):
            cost = prices[high]-min_price
            ans = max(ans,cost)
            if prices[high]<min_price:
                min_price = prices[high]

        return ans        