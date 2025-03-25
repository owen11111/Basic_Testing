import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_pos(self):
        self.assertEqual(add(2, 4), 6)

    def test_add_neg(self):
        self.assertEqual(add(-3, -6), -9)

def add(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    unittest.main()