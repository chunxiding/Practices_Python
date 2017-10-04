class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dict = {}
        dict[nums[0]] = 1
        dict[-nums[0]] = 1
        if nums[0] == 0: dict[0] = 2
        for i in nums[1:]:
            newdict = {}
            for key in dict.keys():
                newdict[key+i] = newdict.get(key+i, 0) + dict[key]
                newdict[key-i] = newdict.get(key-i, 0) + dict[key]
            dict = newdict
        return dict.get(S, 0)
