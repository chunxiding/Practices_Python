class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        start = prices[0]
        maxnum = 0
        
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                continue
            else:
                maxnum += prices[i]-prices[i-1]

        return maxnum
