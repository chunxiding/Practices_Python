class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        binary search
        """
        def binarySearch(nums, target, start, end):
            if end-start+1 <= 0:
                return -1
            mid = start+(end-start)//2
            if nums[mid]==target:
                return mid
            else:
                if target<nums[mid]:
                    return binarySearch(nums,target, start, mid-1)
                else:
	                return binarySearch(nums,target, mid+1, end)
                    
        fstb = binarySearch(nums, target, 0, len(nums)-1)
        if fstb == -1:
            return [-1, -1]
        rtb = fstb
        ltb = fstb
        while nums[rtb] == target:
            if rtb+1 >= len(nums) or nums[rtb+1] > target:
                break
            rtb = binarySearch(nums, target, rtb+1, len(nums)-1)

        while nums[ltb] == target:
            if ltb-1 < 0 or nums[ltb-1] < target:
                break
            ltb = binarySearch(nums, target, 0, ltb)
            
        return [ltb, rtb]
