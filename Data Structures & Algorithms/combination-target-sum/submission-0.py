class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        def solve(i , curr_sum , ans):
            if i>=len(candidates):
                return 
            if curr_sum ==target:
                res.append(ans.copy())
                return 
            if curr_sum>target:
                return 
            ans.append(candidates[i])
            curr_sum+=candidates[i]
            solve(i,curr_sum,ans)
            e = ans.pop()
            curr_sum-=e
            solve(i+1,curr_sum,ans)
        solve(0,0,ans)
        return res
        