class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first = rounds[0]
        last = rounds[-1]
        
        if first <= last:
            return [i for i in range(first, last+1)]
        else:
            res = []
            
            for i in range(n):
                if i+ 1 <= last or i + 1 >= first:
                    res.append(i+1)
            return sorted(res)