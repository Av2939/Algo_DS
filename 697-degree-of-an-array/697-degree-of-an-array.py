class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = {}
        count = {}
        
        for i, x in enumerate(nums):
            
            if x not in left:
                left[x] = i
            
            right[x] = i
            count[x] = 1 + count.get(x, 0)
            
        ans = len(nums)
        degree = max(count.values())
        
        for x in count:
            
            if degree == count[x]:
                ans = min(ans, right[x] - left[x] + 1)
        return ans
                