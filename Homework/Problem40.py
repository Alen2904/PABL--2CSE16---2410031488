class Solution:
    def subsets(self, nums):
        res = []
        subset = []
        
        def dfs(index):
            if index == len(nums):
                res.append(list(subset))
                return
            
            dfs(index + 1)
            
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
        
        dfs(0)
        return res


print(Solution().subsets([1,2,3]))
print(Solution().subsets([0]))