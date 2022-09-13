class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        
        start = rounds[0]
        end = rounds[-1]
        
        
        if start <= end:
            return [i for i in range(start, end+1)]
        
        else:
            
            res = []
            
            for i in range(n):
                
                if i + 1 <= end or i + 1 >= start:
                    res.append(i+1)
                    
            return res