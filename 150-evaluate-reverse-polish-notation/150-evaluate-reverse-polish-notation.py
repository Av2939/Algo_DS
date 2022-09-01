class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            
            if token not in "-+/*":
                stack.append(int(token))
                continue
            
            number_2 = stack.pop()
            number_1 = stack.pop()
            
            res = 0
            if token == "+":
                res = number_1 + number_2
                
            elif token == "-":
                res = number_1 - number_2
            elif token == "*":
                res = number_1 * number_2
            else:
                res = int(number_1/number_2)
            
            stack.append(res)
        
        return stack.pop()
                