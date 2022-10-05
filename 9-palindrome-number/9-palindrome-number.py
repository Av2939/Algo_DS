class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        
        if x_string == x_string[::-1]:
            return True 
        else: 
            return False