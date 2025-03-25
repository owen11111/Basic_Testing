import unittest
from main import mult, div

class TestMult(unittest.TestCase):
    def test_mult_pos(self):
        self.assertEqual(mult(2, 3), 6)

if __name__ == "__main__":
    unittest.main()