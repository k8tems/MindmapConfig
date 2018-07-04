import unittest
import main


class TestCase(unittest.TestCase):
    def test_parse(self):
        input = [
            ('a', (0, 0)), ('b', (1, 1)),
            ('c', (0, 2)), ('d', (1, 3))]
        expected = [
            {'children': [{
                'children': [],
                'id': None,
                'side': 'left',
                'text': 'b'}],
             'id': None,
             'side': 'left',
             'text': 'a'},
            {'children': [
                {'children': [],
                 'id': None,
                 'side': 'left',
                 'text': 'd'}],
             'id': None,
             'side': 'left',
             'text': 'c'}]
        self.assertEqual(expected, main.parse(input))

    def test_search_parent(self):
        c_node = {
            'children': [],
            'id': None,
            'side': 'left',
            'crd': (2, 2),
            'text': 'c'}
        b_node = {
            'children': [c_node],
            'id': None,
            'crd': (1, 1),
            'side': 'left',
            'text': 'b'}
        a_node = {
            'children': [b_node],
            'id': None,
            'crd': (0, 0),
            'side': 'left',
            'text': 'a'}
        mind_map = [a_node]
        expected = [b_node]
        self.assertEqual(expected, main.search_parent_candidates(mind_map, (2, 2)))


if __name__ == '__main__':
    unittest.main()
