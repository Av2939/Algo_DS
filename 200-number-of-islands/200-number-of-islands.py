class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r,c):
            visit.add((r,c))
            queue = collections.deque()
            queue.append((r,c))
            
            while queue:
                row,col = queue.popleft()
                
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if (r in range (rows) and c in range (cols) and
                        (r,c) not in visit and
                        grid[r][c] == "1"):
                        
                        visit.add((r,c))
                        queue.append((r,c))
                        
                
                
        
        for r in range (rows):
            for c in range (cols):
                
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
                    
        return islands
                    
                    
        
        