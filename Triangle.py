class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        triangle[i][j] connects to triangle[i+1][j] & [j+1]
        :rtype: int
        """
        dp = triangle
        
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] += dp[i-1][0]
                elif j == i:
                    dp[i][j] += dp[i-1][-1]
                else:
                    dp[i][j] += min(dp[i-1][j-1], dp[i-1][j])
        print dp
        return min(dp[-1][:])
