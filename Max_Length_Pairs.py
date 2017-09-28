class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        sort first, ensure start with lowest
        """
        """
        worked but time limit exceed in last
        # number of pairs in chain ending here
        dp = [1 for _ in range(len(pairs))]
        pairs = sorted(pairs, key = lambda x: x[1])
        print pairs
        start = pairs[0][0]
        end = pairs[0][1]
        length = 1
        
        for i in range(1, len(pairs)):
            # cases where can be added to the longest one
            if pairs[i][0] > end:
                end = pairs[i][1]
                dp[i] = length + 1
                length += 1
            else: 
            # backtracking -> insert in middle
                for j in range(i):
                    if pairs[i][0] > pairs[j][1]:
                        dp[i] = dp[j]+1
        
        return max(dp[:])
        """
        #edited so that backtracking only need the first find one
        dp = [1 for _ in range(len(pairs))]
        pairs = sorted(pairs, key = lambda x: x[1])
        end = pairs[0][1]
        length = 1
        
        for i in range(1, len(pairs)):
            # cases where can be added to the longest one
            if pairs[i][0] > end:
                end = pairs[i][1]
                dp[i] = length + 1
                length += 1
            else: 
            # backtracking -> insert in middle
                for j in range(i-1, 1, -1):
                    if pairs[i][0] > pairs[j][1]:
                        dp[i] = dp[j]+1
                        break
        
        return max(dp[:])
