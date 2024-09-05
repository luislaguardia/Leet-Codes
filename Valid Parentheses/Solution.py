class Solution(object):
    def isValid(self, s):

        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'

                if bracket_map[char] != top_element: #xD
                    return False
            else:
                stack.append(char)
        return not stack
