class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        min_len = float('inf')
        s_index = -1
        freq = {}
        for i in t:
            freq[i] = freq.get(i,0)+1
        high = 0
        low = 0
        count = 0
        while high<n:
            if s[high] in freq:
                if freq[s[high]]>0:
                    count+=1
                freq[s[high]]-=1
            while count==m:
                if (high-low+1)<min_len:
                    min_len = high-low+1
                    s_index = low
                if s[low] in freq:
                    freq[s[low]]+=1
                    if freq[s[low]]>0:
                        count-=1
                low+=1
            high+=1
        return "" if s_index==-1 else s[s_index:min_len+s_index]        