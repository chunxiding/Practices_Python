# 9/22/2017
# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
# Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums == None or len(nums) == 0 or k<0:
            return 0
        
        dict = {}
        result = 0
        
        for i in nums:
            if dict.has_key(i):
                dict[i] += 1
            else:
                dict[i] = 1
        
        if k == 0:
            for key in dict.keys():
                if dict[key] >= 2:
                    result += 1
        else:
            for key in dict.keys():
                if dict.has_key(key+k):
                    result += 1
        
        return result
