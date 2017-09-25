class Solution(object):
    def rotate(self, matrix):
        """
        first transpose
        than flip
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        temp = 0
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][-j-1]
                matrix[i][-j-1] = temp
