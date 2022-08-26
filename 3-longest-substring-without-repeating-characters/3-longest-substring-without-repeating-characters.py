class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxS = 0
        l = 0
        hashSet = set()
        
        for r in range(len(s)):
            
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            
            hashSet.add(s[r])
            maxS = max(maxS, r-l+1)
        
        return maxS
                
            