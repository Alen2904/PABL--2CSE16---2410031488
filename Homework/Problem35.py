from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            res[key].append(s)
        return list(res.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))