class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        rows, cols = len(matrix), len(matrix[0])
        
        bot, top = rows-1, 0
        
        while top <= bot:
            
            row = (bot + top)//2
            
            if target > matrix[row][-1]:
                top = row + 1
            
            elif target < matrix[row][0]: 
                bot = row -1 
                
            else:
                break
                
        l, r = 0, cols-1
        
        row = (top+bot)//2
        
        
        while l <= r:
            mid = (l+r)//2
            
            if target < matrix[row][mid]:
                r = mid -1
            
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
            
        
        return False
                
        
        
        
        
        