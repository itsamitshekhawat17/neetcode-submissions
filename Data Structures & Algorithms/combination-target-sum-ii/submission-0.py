class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        candidates.sort()
        n = len(candidates)
        def solve(imdx , total):
            if total ==0:
                res.append(ans.copy())
                return 
            for i in range(imdx,n):
                if i>imdx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>total:
                    break
                ans.append(candidates[i])
                solve(i+1,total - candidates[i])
                ans.pop()
        solve(0,target)
        return res
           
