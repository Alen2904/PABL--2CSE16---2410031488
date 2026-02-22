import bisect

class Solution:
    def median(self, mat):
        if not mat or not mat[0]:
            raise ValueError("Empty matrix")
        r = len(mat)
        c = len(mat[0])
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        desired = (r * c) // 2
        ans = low
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid)
            if count > desired:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

# Example usages
mat1 = [[1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]]
print(Solution().median(mat1))  # 5

mat2 = [[2, 4, 9],
        [3, 6, 7],
        [4, 7, 10]]
print(Solution().median(mat2))  # 6

mat3 = [[3],
        [4],
        [8]]
print(Solution().median(mat3))  # 4