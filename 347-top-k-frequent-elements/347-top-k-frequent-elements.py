class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        Count = {}
        
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            Count[num] = 1 + Count.get(num, 0)
            
        
        for n,c in Count.items():
            freq[c].append(n)
            
        
        res = []
        
        
        for i in range(len(freq)-1, 0, -1):
            
            for j in freq[i]:
                res.append(j)
            
            if len(res) == k:
                return res