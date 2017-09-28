class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        dp on all possibles end with ith
        store in dp the remainders of a subarray end there
        """
        if len(nums) <= 1: return False
        
        if nums == [0, 0]: return True
        
        if k == 0: return False
        
        """
        worked, time limit exceeded
        
        dp = [[] for _ in range(len(nums))]
        dp[0].append(nums[0] % k)
        for i in range(1, len(nums)):
            dp[i].append(nums[i] % k)
            for j in dp[i-1]:
                if (nums[i] % k + j) % k == 0:
                    return True
                else:
                    dp[i].append((nums[i] % k + j) % k)
        return False
        """
        
        # Note that for sum from start to ith, if have same
        # remainder, than the in between there is an answer
        
        dp = [-1 for _ in range(len(nums))]
        dp[0] = (nums[0] % k)
        for i in range(1, len(nums)):
            dp[i] = ((nums[i] + dp[i-1]) % k)
            if dp[i] == 0 or dp[i] in dp[:i]:
                return True
        return False
