class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(path):
            if len(path)==len(nums):
                res.append(path.copy())
                return 
            for num in nums:
                if num in path:
                    continue 
                path.append(num)
                solve(path)
                path.pop()
        solve([])
        return res
