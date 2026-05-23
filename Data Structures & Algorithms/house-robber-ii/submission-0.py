class Solution:
    def solve(self,arr):
        n = len(arr)
        prev2 = 0
        prev = arr[0]
        for i in range(1,n):
            if i>1:
                curr = max(prev,prev2+arr[i])
            else:
                curr = max(prev,arr[i])
            prev2 = prev
            prev = curr
        return prev
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        nums1 = nums[0:n-1]
        nums2 = nums[1:n]
       
        x = self.solve(nums1)
        y = self.solve(nums2)
        return max(x,y)

