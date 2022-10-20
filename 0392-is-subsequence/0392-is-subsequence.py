class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        s_len = len(s)
        t_len = len(t)
        
        match = 0
        
        if s_len == 0:
            return True
        if t_len == 0:
            return False
        
        for i in range(0,len(t)):
            
            if s[match] == t[i]:
                match +=1
            
            if match == s_len:
                return True
            
        return False