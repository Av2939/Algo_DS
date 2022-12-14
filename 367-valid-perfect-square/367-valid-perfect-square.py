class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l,r = 0, num
        
        while l <= r:
            m = (l+r)//2
            if m * m < num:
                l = m + 1
            elif m * m > num:
                r = m -1
            else:
                return True
            
        return False