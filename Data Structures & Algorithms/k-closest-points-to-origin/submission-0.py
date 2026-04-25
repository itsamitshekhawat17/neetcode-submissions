import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        
        ans = []
        for i in range(n):
            a = ( (points[i][0])**2 + (points[i][1])**2 )**0.5
            heapq.heappush(ans , (a,i))
        res = []
        while k :
            res.append(points[ans[0][1]])
            heapq.heappop(ans)
            k-=1
        return res
        