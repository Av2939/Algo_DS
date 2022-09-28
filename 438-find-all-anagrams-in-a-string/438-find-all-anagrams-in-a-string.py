class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(s) < len(p):
            return []
        
        p_count = {}
        s_count = {}
        
        output = []
        
        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
        
        
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            
            if i >= len(p):
                if s_count[s[i - len(p)]] == 1:
                    del s_count[s[i - len(p)]]
                else:
                    s_count[s[i- len(p)]] -= 1
            
            if p_count == s_count:
                output.append(i-len(p) + 1)
        return output
                