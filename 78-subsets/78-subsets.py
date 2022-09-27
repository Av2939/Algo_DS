class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [[]]
        
        for num in nums:
            
            res += [[num] + i for i in res]
        return res