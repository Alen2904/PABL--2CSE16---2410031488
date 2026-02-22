class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            if val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
# Example usage:
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(Solution().searchMatrix(matrix1, 3))   
print(Solution().searchMatrix(matrix1, 13))  