class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        nums.sort()
        res = []
        
        for i, n in enumerate(nums):
            
            if i > 0 and nums[i-1] == n:
                continue
                
            l = i + 1
            r = len(nums)-1
            
            while l<r:
                
                three_sum = n + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
                    
                    
                
        