import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        # Iterate through the string character by character
        for char in s:
            if char in bracket_map:
                # Pop the top element from stack if stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element is the matching opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push it onto the stack
                stack.append(char)

        # The string is valid if the stack is empty at the end
        return not stack


# Unit test class to test the Solution class
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses(self):
        # Test cases where parentheses are valid
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        # Test cases where parentheses are invalid
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))

    def test_empty_string(self):
        # Test an empty string
        self.assertTrue(self.solution.isValid(""))

    def test_mixed_parentheses(self):
        # Test case where parentheses are mixed and invalid
        self.assertFalse(self.solution.isValid("(){"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
