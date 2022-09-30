class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols)
                or grid[r][c] == "0" or (r,c) in visited):
                return 
            visited.add((r,c))
            directions = [(1,0), (0,1), (-1, 0), (0,-1)]
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
                    
        return islands