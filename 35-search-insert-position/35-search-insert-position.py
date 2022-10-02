class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)-1
        
        while l <= r:
            
            mid = (l+r)//2
            
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            
            elif nums[mid] == target:
                return mid

        return l