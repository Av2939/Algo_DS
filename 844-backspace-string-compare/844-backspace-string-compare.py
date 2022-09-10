class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(S):
            res = []
            
            for c in S:
                
                if c != "#":
                    res.append(c)
                elif res:
                    res.pop()
                    
            return "".join(res)
        
        
        return helper(s) == helper(t)