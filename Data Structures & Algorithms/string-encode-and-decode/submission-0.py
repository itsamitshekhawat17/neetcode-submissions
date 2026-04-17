class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res+=str(len(i)) + '#' + i
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i<len(s):
            j =i

            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            j+=1 # to skip #

            word = s[j:j+length]
            res.append(word)

            i = j+length
        return res


