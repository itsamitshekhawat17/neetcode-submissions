class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        for i in s1:
            freq1[i] = freq1.get(i,0)+1
        freq2 = {}
        k = len(s1)
        low = 0
        for high in range(len(s2)):
            freq2[s2[high]] = freq2.get(s2[high],0)+1
            while (high-low+1)>k:
                freq2[s2[low]]-=1
                if freq2[s2[low]]==0:
                    del freq2[s2[low]]
                low+=1
            if (high-low+1)==k:
                if freq2==freq1:
                    return True
        return False        