class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i , n in enumerate(nums):
            freq[n]=i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in freq and freq[diff]!=i:
                return [i,freq[diff]]
        return []
        