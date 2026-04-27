class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        arr = [" "]*n*2
        def solve(i,total):
            if i>=len(arr):
                if total == 0:
                    res.append("".join(arr))
                return
            if total>n:
                return
            if total<0:
                return
            arr[i]="("
            curr_sum = total+1
            solve(i+1,curr_sum)
            arr[i]=")"
            curr_sum = total-1
            solve(i+1,curr_sum)
        solve(0,0)
        return res