class Solution:
    def palindrome(self,s):
        if s==s[::-1]:
            return True
        return False
    def partition(self, s: str) -> List[List[str]]:
        res = []
        ans = []
        n = len(s)
        def solve(s,ans):
            if len(s)==0:
                res.append(ans.copy())
                return
            for i in range(len(s)):
                part = s[0:i+1]
                
                if self.palindrome(part):
                    ans.append(part)
                    solve(s[i+1:],ans)
                    ans.pop()
        solve(s,ans)
        return res