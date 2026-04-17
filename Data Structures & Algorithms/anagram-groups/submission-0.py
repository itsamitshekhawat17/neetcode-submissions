from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            freq[key].append(word)
        return list(freq.values())
        