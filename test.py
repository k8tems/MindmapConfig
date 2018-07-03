import unittest
import main


class TestCase(unittest.TestCase):
    def test_parse(self):
        input = 'a\n    b\nc\n    d'
        expected = [
            {'children': [{'children': [], 'id': None, 'side': 'left', 'text': 'b'}],
             'id': None,
             'side': 'left',
             'text': 'a'},
            {'children': [{'children': [], 'id': None, 'side': 'left', 'text': 'd'}],
             'id': None,
             'side': 'left',
             'text': 'c'}]
        self.assertEqual(expected, main.parse(input))


if __name__ == '__main__':
    unittest.main()
