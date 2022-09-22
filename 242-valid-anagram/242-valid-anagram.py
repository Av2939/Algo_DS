class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        if len(s) != len(t):
            return False
        
        
        sDict = {}
        tDict = {}
        
        for i in range(len(s)):
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)
            
        
        for val in sDict:
            if sDict[val] != tDict.get(val, 0):
                return False
            
        return True
            