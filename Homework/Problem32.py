class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        comb = []

        def dfs(start, remaining):
            if remaining == 0:
                res.append(list(comb))
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > remaining:
                    break
                comb.append(val)
                dfs(i, remaining - val)
                comb.pop()

        dfs(0, target)
        return res

print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))
print(Solution().combinationSum([2], 1))