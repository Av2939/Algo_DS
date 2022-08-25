class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalnum():
                string += c
        lower_s = string.lower()
        
        neg_lower_s = lower_s[::-1]
        
        if lower_s == neg_lower_s:
            return True
        else:
            return False