from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        ans = []
        b =sorted(a.items(), key = lambda x:x[1])
        c = b[::-1]
        for i in range(k):
            ans.append(c[i][0])
            
            
                
        return ans

        