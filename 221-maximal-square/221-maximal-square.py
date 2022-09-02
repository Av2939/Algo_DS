class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        
        def rec(r,c):
            
            if r >= rows or c >= cols:
                return 0
            
            if (r,c) not in memo:
                right = rec(1+r, c)
                down = rec(r, c+1)
                diag = rec(r+1,c+1)
                
                memo[(r,c)] = 0
                
                if matrix[r][c] == "1":
                    memo[(r,c)] = 1 + min(right, down, diag)
            return memo[(r,c)]
        
        
        
        rec(0,0)
        return max(memo.values())**2