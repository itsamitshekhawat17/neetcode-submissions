class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for num,count in freq.items():
            bucket[count].append(num)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res