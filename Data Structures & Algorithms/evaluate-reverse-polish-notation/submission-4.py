class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ("+", "-", "*", "/"):
                stack.append(int(t))
            else:
                match t:
                    case "+":
                        stack.append(stack.pop() + stack.pop())
                    case "-":
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(b - a)
                    case "*":
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(b * a)
                    case "/":
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(int(b / a))
        
        return stack[0]

