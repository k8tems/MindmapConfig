import unittest
import main


class TestCase(unittest.TestCase):
    def test_parse(self):
        input = [
            ('a', 0), ('b', 1),
            ('c', 0), ('d', 1)]
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
