class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        freq = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        res = []
        ans = []
        if len(digits)==0:
            return []
        def solve(i,ans):
            if i>=len(digits):
                res.append("".join(ans))
                return 
            for ch in freq[digits[i]]:
                ans.append(ch)
                solve(i+1,ans)
                ans.pop()
        solve(0,ans)
        return res