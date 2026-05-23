class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev = nums[0]
        for i in range(1,n):
            if i>1:
                curr = max(prev,prev2+nums[i])
            else:
                curr = max(prev,nums[i])
            prev2 = prev
            prev = curr
        return prev

        