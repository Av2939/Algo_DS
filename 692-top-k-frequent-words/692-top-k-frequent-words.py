class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = {}
        heap = []
        
        for word in words:
            count[word] = 1 + count.get(word, 0)
            
        
        heap = [(-freq, word) for word, freq in count.items()]
        
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
        