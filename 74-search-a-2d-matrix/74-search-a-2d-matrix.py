class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        
        top, bot = 0, rows-1
        
        while top <= bot:
            row = (top+bot)//2
            
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break
        
        
        row = (top+bot)//2
        l,r = 0, cols-1
        
        while l <= r:
            
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid + 1
            
            elif target < matrix[row][mid]:
                r = mid -1
            else:
                return True
        
        return False