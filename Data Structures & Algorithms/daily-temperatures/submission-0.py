class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0]*n # i can only append in empty list 
        stack = []
        for i in range(len(arr)):
            while len(stack)!=0 and arr[i]>arr[stack[-1]]:
                index = stack.pop()
                ans[index] = i-index
            stack.append(i)
        return ans
