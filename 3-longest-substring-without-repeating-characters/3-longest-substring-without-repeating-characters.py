class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxS = 0 
        charSet = set()
        l = 0
        
        for r in range(len(s)):
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            maxS = max(maxS, r-l+1)
            
        return maxS
    
    #O(n) time O(m) space, m being the lenght of the longest substring