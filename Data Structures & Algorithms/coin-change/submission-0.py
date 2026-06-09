class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf') for _ in range(amount+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0]=0
        for j in range(1,amount+1):
            if j%coins[0]==0:
                dp[0][j]=j//coins[0]
        for i in range(1,n):
            for j in range(1,amount+1):
                if coins[i]>j:
                    pick = float('inf')
                else:
                    pick = 1+ dp[i][j-coins[i]]
                not_pick = dp[i-1][j]
                dp[i][j] = min(pick , not_pick)
        ans = dp[n-1][amount]
        return -1 if ans==float('inf') else ans