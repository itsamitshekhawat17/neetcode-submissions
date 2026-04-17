class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if i.isalnum():
                ans+=i.lower()
        if ans==ans[::-1]:
            return True
        return False
        
        