# in python 3.7, can sort dict by
# sorted(dict, key=dict.get)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        lst = []
        
        for i in nums:
            if dict.has_key(i):
                dict[i] += 1
            else:
                dict[i] = 1
        
        lst = sorted(dict, key=dict.get, reverse = True)
        return lst[:k]
