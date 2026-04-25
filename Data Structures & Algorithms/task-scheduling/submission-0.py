from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # created a max heap and inserted negativee values 
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        q = deque()
        time = 0

        while maxheap or  q:
            time+=1

            if maxheap:
                cnt = heapq.heappop(maxheap)+1 #why 1 -> to reduce the count 
                if cnt!=0:
                    q.append((cnt,time+n)) # time+n -> next time available when?
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])#push the cnt back to the heap 
        return time



