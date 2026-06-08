class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr_sum = sum(nums)
        if (arr_sum-target)%2!=0 or (arr_sum-target)<0:
            return 0
        total = (arr_sum - target)//2
        dp = [[0 for _ in range(total+1)] for _ in range(n+1)]
        dp[0][0]=1
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(total+1):
                not_pick = dp[i-1][j]
                if nums[i-1]>j:
                    pick = 0
                else:
                    pick = dp[i-1][j-nums[i-1]]
                dp[i][j] = not_pick+pick
        return dp[n][total]
        