class Solution:
    def rowWithMaxOnes(self, arr):
        if not arr or not arr[0]:
            return -1
        n = len(arr)
        m = len(arr[0])
        max_row = -1
        j = m - 1
        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                max_row = i
                j -= 1
        return max_row

# Example runs
arr1 = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
arr2 = [[0,0], [1,1]]
arr3 = [[0,0], [0,0]]

print(Solution().rowWithMaxOnes(arr1))  # 2
print(Solution().rowWithMaxOnes(arr2))  # 1
print(Solution().rowWithMaxOnes(arr3))  # -1