# Solution class to convert Roman numerals to integers
class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to their corresponding integer values
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        
        # Iterate through the string in reverse (from right to left)
        for char in reversed(s):
            current_value = roman_map[char]
            
            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Update the previous value for the next iteration
            prev_value = current_value
        
        return total


# Unit test class to test the Solution class
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
