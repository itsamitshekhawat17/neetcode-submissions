class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0 
        arr = set(nums)
        
        ans = 0

        for i in arr:
            if i-1 not in arr:
                curr = i
                count = 1
                while curr+1 in arr:
                    curr+=1
                    count+=1
                ans = max(ans,count) 
        return ans