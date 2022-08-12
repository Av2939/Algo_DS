class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0,0,1)]) #steps, position, speed
        seen = set()
        
        while queue:
            
            steps, position, speed = queue.popleft()
            
            if (position, speed) in seen:
                continue
            
            seen.add((position, speed))
            
            if position == target:
                return steps
            
            queue.append((steps + 1, position + speed, speed *2))
            
            if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                
                speed = -1 if speed > 0 else 1
                queue.append((steps + 1, position, speed))
            
            
        
        
        
        