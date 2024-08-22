class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                numStack.append(int(t))
            else:
                b = numStack.pop()
                a = numStack.pop()
                
                if t == "+":
                    numStack.append(a + b)
                elif t == "-":
                    numStack.append(a - b)
                elif t == "*":
                    numStack.append(a * b)
                elif t == "/":
                    numStack.append(int(a / b))
                    
        return numStack[0]