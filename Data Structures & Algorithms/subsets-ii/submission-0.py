class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        n = len(nums)
        nums.sort()
        def solve(indx,ans):
            res.append(ans.copy())
            for i in range(indx,n):
                if i>indx and nums[i]==nums[i-1]:
                    continue 
                ans.append(nums[i])
                solve(i+1,ans)
                ans.pop()
        solve(0,ans)
        return res
     