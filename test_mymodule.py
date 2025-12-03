"""
Unit tests for the 'square' and 'double' functions imported from mymodule.
This module uses the built-in 'unittest' framework.
"""
import unittest
from mymodule import square, double


class TestSquare(unittest.TestCase):
    """Test suite for the square function."""  # Test suite for square.

    def test_square_values(self):
        """Tests 'square' with positive, float, and negative inputs."""

        # Use hanging indents to prevent E501/C0301 errors.
        self.assertEqual(square(2), 4,
                         "Expected square(2) to be 4.")  # Test for 2.

        self.assertEqual(square(3.0), 9.0,
                         "Expected square(3.0) to be 9.0.")

        # E501 and E261 fixed by using a hanging indent.
        self.assertNotEqual(
            square(-3),
            -9,
            "Expected square(-3) NOT to be -9 (should be 9)."
        )


class TestDouble(unittest.TestCase):
    """Test suite for the double function."""  # Test suite for double.

    def test_double_values(self):
        """Tests 'double' with positive, negative float, and zero inputs."""

        self.assertEqual(double(2), 4,
                         "Expected double(2) to be 4.")  # Test for 2.

        self.assertEqual(double(-3.1), -6.2,
                         "Expected double(-3.1) to be -6.2.")  # Test for -3.1.

        self.assertEqual(double(0), 0,
                         "Expected double(0) to be 0.")  # Test for 0.


# Run all the test cases defined in the module when the script is executed.
if __name__ == '__main__':
    unittest.main()  # Main test runner.
