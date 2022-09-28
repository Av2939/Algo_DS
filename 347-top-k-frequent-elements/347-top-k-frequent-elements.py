class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        elementCount = {}
        
        for num in nums:
            
            elementCount[num] = 1 + elementCount.get(num, 0)
            
        
        pQueue = [[-count, element] for element, count in elementCount.items()]
        
        heapq.heapify(pQueue)
        
        return [heapq.heappop(pQueue)[1] for i in range(k)]