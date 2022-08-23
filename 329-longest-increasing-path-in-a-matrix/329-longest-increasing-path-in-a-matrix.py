class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(r,c, prevVal):
            
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                matrix[r][c] <= prevVal):
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            res = 0
            
            res = max(res, 1+dfs(r+1, c, matrix[r][c]))
            res = max(res, 1+dfs(r-1, c, matrix[r][c]))
            res = max(res, 1+dfs(r, c+1, matrix[r][c]))
            res = max(res, 1+dfs(r, c-1, matrix[r][c]))
            
            memo[(r,c)] = res
            
            return res
            
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c, -1)
                
        return max(memo.values())