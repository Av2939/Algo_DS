class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        
        def backtracking(first = 0, curr = []):
            
            if len(curr) == k:
                res.append(curr[:])
                
            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtracking(i+1, curr)
                curr.pop()
            
        for k in range(len(nums)+1):
            backtracking()
        
        return res