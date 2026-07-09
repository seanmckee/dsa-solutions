class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if len(stack) == 0: return False
                if matches[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        