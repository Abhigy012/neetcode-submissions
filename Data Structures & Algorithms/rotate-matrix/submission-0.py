class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i , n):
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = a
        
        
        # reversing
        for i in range (n):
            matrix[i].reverse()