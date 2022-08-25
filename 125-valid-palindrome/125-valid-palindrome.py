class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = ""
        
        for c in s:
            
            if c.isalnum():
                string+= c
        
        low_s = string.lower()
        
        if low_s != low_s[::-1]:
            return False
        return True