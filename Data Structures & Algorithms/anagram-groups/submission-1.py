from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        # for word in strs:
        #     key = "".join(sorted(word))
        #     freq[key].append(word)
        # return list(freq.values())
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            key = tuple(count)
            freq[key].append(word)
        return list(freq.values())        