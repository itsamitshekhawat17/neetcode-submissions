class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(amount+1):
                if coins[i-1]>j:
                    pick = 0
                else:
                    pick = dp[i][j-coins[i-1]]
                not_pick = dp[i-1][j]
                dp[i][j] = pick + not_pick
        return dp[n][amount]
                
             