class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        comb = []

        def dfs(start, remaining):
            if remaining == 0:
                res.append(list(comb))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                val = candidates[i]
                if val > remaining:
                    break
                comb.append(val)
                dfs(i + 1, remaining - val)
                comb.pop()

        dfs(0, target)
        return res

# Example usage
print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
print(Solution().combinationSum2([2,5,2,1,2], 5))