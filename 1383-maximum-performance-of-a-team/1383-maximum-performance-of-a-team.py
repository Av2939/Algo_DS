class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7
        
        canidates = zip(efficiency, speed)
        canidates = sorted(canidates, key = lambda i : i[0], reverse = True)
        
        speed_heap = []
        speed_sum, perf = 0,0 
        
        for cur_eff, cur_speed in canidates:
            
            if len(speed_heap) >= k:
                speed_sum -= heapq.heappop(speed_heap)
                
            heapq.heappush(speed_heap, cur_speed)
            
            speed_sum += cur_speed
            perf = max(perf, speed_sum * cur_eff)
            
        return perf%modulo