class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        target = (rows-1, cols-1)
        
        state = (0,0,k) # row, col, elims
        visited = set([state])
        queue = collections.deque([(0, state)]) #steps, state
        
        while queue:
            steps, (row, col, k) = queue.popleft()
            
            if (row, col) == target:
                return steps
            
            
            for new_row, new_col in [(row+1, col), (row-1, col), (row, col+1),(row, col-1)]:
                if (0<= new_row < rows) and (0 <= new_col < cols):
                
                    new_eliminations = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)

                    if new_eliminations >= 0 and new_state not in visited:
                        visited.add(new_state)
                        queue.append((steps+1, new_state))
                    
                    
        return -1