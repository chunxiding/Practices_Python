class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        need to be congruent
        go through, store number of strings end with each alphabet
        this number equals to the number of substrings can be found
        """
        dp = [0]*26
        
        count = 0
        
        for i in range(len(p)):
            if i == 0:
                count += 1
                dp[ord(p[i])-97] = max(dp[ord(p[i])-97], count)
            if i > 0:
                if (ord(p[i]) - ord(p[i-1]) == 1) or (ord(p[i]) - ord(p[i-1]) == -25):
                    count += 1
                else:
                    count = 1
                dp[ord(p[i])-97] = max(dp[ord(p[i])-97], count)
        print dp
        
        return sum(dp[:])
