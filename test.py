import unittest
import main


class TestCase(unittest.TestCase):
    def test(self):
        input = 'a\n    b\nc\n    d'
        expected = {'a': ['b'], 'c': ['d']}
        self.assertEqual(expected, main.parse(input))


if __name__ == '__main__':
    unittest.main()
