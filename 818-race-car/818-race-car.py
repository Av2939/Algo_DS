class Solution:
    def racecar(self, target: int) -> int:
        seen = set()
        queue = collections.deque([(0,0,1)]) #steps, position, speed
        
        while queue:
            steps, position, speed = queue.popleft()
            
            if (position, speed) in seen:
                continue
            
            queue.append((steps+1, position+speed, speed * 2))
            seen.add((position, speed))
            
            if position == target:
                return steps
            
            else:
                
                if ((position + speed < target and speed < 0) or (position + speed > target and speed > 0)):
                    
                    speed = -1 if speed >0 else 1
                    
                    queue.append((steps+1, position, speed))
                