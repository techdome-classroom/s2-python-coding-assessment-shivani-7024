class Solution:
    def isValid(self, s: str)->bool:

        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

         for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

        import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_mixed_parentheses(self):
        # Test case where parentheses are mixed and invalid
        self.assertFalse(self.solution.isValid("(){"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)







    



  

