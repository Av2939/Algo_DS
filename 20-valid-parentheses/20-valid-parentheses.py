class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        Mapping = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for c in s:
            if c not in Mapping:
                stack.append(c)
                continue
            
            if not stack or stack[-1] != Mapping[c]:
                return False
            stack.pop()
        
        return not stack
                