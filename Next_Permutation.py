class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        if descending, return asending
        find the first number from back, that is smaller than its next number.
        exchange it with the next bigger number in the back.
        then sort the rest of the numbers in the back.
        123456
        654321
        123546 - 123564
        234165 - 234516
        123564 - 123645
        """
        
        
        
        nums1 = nums
        i = len(nums)-1
        temp = 0
        
        while i-1 >= 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        
        
        
                
        temp = nums[i-1]
        nextb = max(nums[i:])
        for number in nums[i:]:
            if number > temp:
                nextb = min(number, nextb)
        nums[i-1] = nextb
        nums[i + nums[i:].index(nextb)] = temp
        nums[i:] = sorted(nums[i:])
        
        if nums == sorted(nums1, reverse = True):
            nums = sorted(nums)
