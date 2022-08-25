class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        
        for c in s:
            
            if c.isalnum():
                res += c
        s_lower = res.lower()
        
        if s_lower != s_lower[::-1]:
            return False
        
        return True
    
    #This technically takes up more space then using two pointers.
    #But it's a lot more cleaner
        