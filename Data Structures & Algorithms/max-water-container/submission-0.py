class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = float('-inf')
        n = len(height)
        low = 0
        high = n-1
        while low<high:
            h = min(height[low],height[high])
            w = high - low
            area = h*w
            ans = max(area,ans)
            if height[low]<height[high]:
                low+=1
            else:
                high-=1
        return ans

        
        