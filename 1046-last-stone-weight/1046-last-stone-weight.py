class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-i for i in stones]
        
        heapq.heapify(heap)
        
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            
            if second > first:
                heapq.heappush(heap, first-second)
                
        heap.append(0)
            
        return abs(heap[0])