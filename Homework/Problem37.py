class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix1)
print(matrix1)

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix2)
print(matrix2)