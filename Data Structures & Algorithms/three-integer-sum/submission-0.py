class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        res = []
        for i in range(n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            low = i+1
            high = n-1
            while low<high:
                total = arr[i] + arr[low] + arr[high]
                if total==0:
                    res.append([arr[i],arr[low],arr[high]])
                    while low<high and arr[low]==arr[low+1]:
                        low+=1
                    while low<high and arr[high]==arr[high-1]:
                        high-=1
                    high-=1
                    low+=1
                elif total>0:
                    high-=1
                else:
                    low+=1
        return res
        