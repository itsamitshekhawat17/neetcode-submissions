class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        def solve(i,ans):
            if i>=len(nums):
                res.append(ans.copy())
                return 
            ans.append(nums[i])
            solve(i+1,ans)
            ans.pop()
            solve(i+1,ans)
        solve(0,ans)
        return res