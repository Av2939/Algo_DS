class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        Sett = set()
        
        for num in nums:
            
            if num in Sett:
                return True
            
            Sett.add(num)