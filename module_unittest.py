"""
This is the "somemodule" module. It contains a function, square(),
that calculates and returns its input squared. For example,

>>> square(3)
9

It also contains a function, half(), that calculates and returns half
of its input (as a float). THIS FUNCTION IS DESIGNED TO FAIL! For
example,

>>> half(3)
1.5
"""
import unittest

class TestTheFunctions(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(3), 9)

    def test_half(self):
        self.assertEqual(half(3), 1.5)

def square(x):
    return x**2

def half(x):
    return float(x)/2 + 1

if __name__ == "__main__":
    unittest.main()
