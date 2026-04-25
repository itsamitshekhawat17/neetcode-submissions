import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        ans = []
        for i in range(n):
            heapq.heappush(ans,-stones[i])
        while len(ans)>1:

            x = -heapq.heappop(ans)
            y = -heapq.heappop(ans)
            if x!=y:
                heapq.heappush(ans,-(x-y))
        return -ans[0] if ans else 0

            
        