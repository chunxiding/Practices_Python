class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        since can only walk down and right
        if their is an obstacle than every block after that is 0
        """
        
        dp = [[0 for x in range(len(obstacleGrid[0]))] for y in range (len(obstacleGrid))]
        print dp

        # first line
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            elif obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
        print dp
        
        # first row
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            elif obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                break
                
        print dp
       
        # DP propagation
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        print dp
        
        return dp[-1][-1]
