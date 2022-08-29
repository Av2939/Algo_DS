class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexQ = deque()
        valQ = deque()
        res = []
        
        for i, n in enumerate(nums):
            
            while valQ and valQ[-1] < n:
                valQ.pop()
                indexQ.pop()
            indexQ.append(i)
            valQ.append(n)
            
            while i - indexQ[0] + 1 > k:
                indexQ.popleft()
                valQ.popleft()
            
            if i + 1 >= k:
                res.append(valQ[0])
        return res