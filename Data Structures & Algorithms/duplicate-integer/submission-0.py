class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        n = len(nums)
        for  i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for i in freq:
            if freq[i]>1:
                return True
        return False
        