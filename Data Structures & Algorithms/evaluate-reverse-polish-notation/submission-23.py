class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = set(["+","-","*","/"])
        stack = []

        def calc(sign):
            right = stack.pop()
            left = stack.pop()
            if sign == "+":
                return left + right
            elif sign == "-":
                return left - right
            elif sign == "*":
                return left * right
            elif sign == "/":
                return int(left / right)
        
        for token in tokens:
            if token in signs:
                val = calc(token)
                stack.append(int(val))
                continue
            stack.append(int(token))
        return stack[0] 

        
