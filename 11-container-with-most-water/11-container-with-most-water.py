class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        
        l = 0
        r = len(height)-1
        
        while l < r:
            water = min(height[l], height[r]) *(r-l) 
            maxWater = max(maxWater, water)
            
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return maxWater
    