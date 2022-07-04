class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top_of_stack = stack.pop()
                if char == ")" and top_of_stack != "(":
                    return False
                if char == "}" and top_of_stack != "{":
                    return False
                if char == "]" and top_of_stack != "[":
                    return False
        return len(stack) == 0
