class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            current_value = roman_map[char]
            
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value
        
        return total

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_numerals(self):
        self.assertEqual(self.solution.romanToInt("I"), 1)
        self.assertEqual(self.solution.romanToInt("V"), 5)
        self.assertEqual(self.solution.romanToInt("X"), 10)

    def test_complex_numerals(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)

    def test_large_numerals(self):
        self.assertEqual(self.solution.romanToInt("MMMDCCCLXXXVIII"), 3888)
        self.assertEqual(self.solution.romanToInt("MMMCMXCIX"), 3999)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)