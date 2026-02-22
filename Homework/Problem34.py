class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        current_end = 0
        furthest = 0
        for i in range(n - 1):
            if i + nums[i] > furthest:
                furthest = i + nums[i]
            if i == current_end:
                jumps += 1
                current_end = furthest
        return jumps
print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,3,0,1,4]))