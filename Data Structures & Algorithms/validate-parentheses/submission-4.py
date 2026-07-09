class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'[': ']', '(': ')', '{': '}'}
        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            else:
                if stack and ch in pairs.values():
                    if ch == pairs[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return not stack