class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap_min, self.k = nums, k
        heapq.heapify(self.heap_min)
        
        while len(self.heap_min) > self.k:
            heapq.heappop(self.heap_min)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        heapq.heappush(self.heap_min, val)
        
        while len(self.heap_min) > self.k:
            heapq.heappop(self.heap_min)
            
        return self.heap_min[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)