import unittest
from Gradient import Gradient

# autocmd BufWritePost <buffer> !python3 runTests.py

class TestGradient(unittest.TestCase):
    grad = Gradient()
    def test_getColor(self):
        self.assertEqual(self.grad.getColor(0),'#ffe4b5')
        self.assertEqual(self.grad.getColor(36), '#63ff3d')
        self.assertEqual(self.grad.getColor(95), '#002277')
        self.assertIsNone(self.grad.getColor(100))

    def test_getLength(self):
        self.assertEqual(self.grad.getLength(), 96)


if __name__ == '__main__':
    unittest.main()