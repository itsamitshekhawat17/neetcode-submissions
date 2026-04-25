import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.ans = nums
        heapq.heapify(self.ans)

        while len(self.ans)>k:
            heapq.heappop(self.ans)

    def add(self, val: int) -> int:
        heapq.heappush(self.ans,val)
        
        while len(self.ans)>self.k:
            heapq.heappop(self.ans)
        return self.ans[0]
        
   
            
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)