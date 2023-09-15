# https://leetcode.com/problems/valid-parentheses/

class Solution:
    # @param1: string of parantheses
    # return: bool, valid: True/False
    def isValid(self, s: str) -> bool:
        # maintain the list of all parantheses
        braces = '({['
        # maintain the map from open to close
        cTo = {')': '(', '}': '{', ']': '['}
        # surprise! this is a stack problem :)
        stack = []
        for i in range(len(s)):
            # if current character is an open parantheses
            # push it to stack
            if s[i] in braces:
                stack.append(s[i])
            else:
                # if not, it must be a close paranthesis
                # problem states string only has parantheses
                # if stack is empty at this point, we don't have a matching open
                # so invalid
                if len(stack) == 0:
                    return False
                # pop the top of the stack
                top = stack.pop()
                # see if it matches the current closing
                if top != cTo[s[i]]:
                    return False
        # if there is a leftover in the stack, more open brackets (then also invalid)
        if len(stack) != 0:
            return False
        # after handling all invalid cases, the string is valid!
        return True

    # time complexity: O(n)
    # space complexity: O(n)
