class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                ch = stack.pop()
                if (ch=='(' and s[i]==')') or (ch=='[' and s[i]==']') or (ch=='{' and s[i]=='}'):
                    continue
                else:
                    return False
        return len(stack)==0
        