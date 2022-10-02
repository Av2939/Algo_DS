class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        j=0
        while(n>j):
            j=j+1
            n=n-j
        return j