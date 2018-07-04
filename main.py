"""
Convert indented mindmap to the format that can understood by
https://github.com/ondras/my-mind
"""

import json
from copy import deepcopy


def split_indent(line):
    num_spaces = 0
    for l in line:
        if l != ' ':
            break
        num_spaces += 1
    assert(num_spaces % 4 == 0)
    return line[num_spaces:], num_spaces // 4


def search_parent_candidates(mind_map, crd, candidates=None):
    """
    Search the mind map exhaustively for parent node candidates
    Every node that has 1 less indent and is above the child is considered a candidate
    This is obviously inefficient and unscalable but it should be OK as I'm not expecting too much data
    """
    candidates = candidates or []

    for node in mind_map:
        candidates += search_parent_candidates(node['children'], crd, candidates)
        node_x, node_y = node['crd']
        if crd[0] - node_x == 1 and node_y < crd[1]:
            candidates.append(node)

    return candidates


def elect(candidates):
    """
    Select the candidate that has the highest y value
    i.e. is closest to the child
    """
    return max(candidates, key=lambda x: x['crd'][1]) if candidates else None


def remove_crds(mind_map):
    for node in mind_map:
        remove_crds(node['children'])
        del node['crd']
    return mind_map


def parse(input, mind_map):
    """Convert input data to the format that can be understood by `my-mind`"""
    node_base = {'children': [], 'id': None, 'side': 'left', 'text': None, 'crd': None}

    for text, (x, y) in input:
        node = deepcopy(node_base)
        node['text'] = text
        # Add coordinate information to simplify the search process
        # Should be cleaned up with `remove_crds` prior to returning
        node['crd'] = (x, y)
        parent = elect(search_parent_candidates(mind_map, (x, y)))

        if not parent:
            parent = mind_map

        parent['children'].append(node)

    return remove_crds(mind_map)


def preprocess(text):
    """
    Convert input data to a list of (node text, (x, y))
    """
    result = []

    for i, line in enumerate(text.split('\n')):
        text, num_indent = split_indent(line)
        result.append((text, (num_indent, i)))

    return result


def main():
    mind_map = {
        'root': {'id': "hyfkdnca",
                 'text': 'My Mind Map',
                 'layout': 'map',
                 'children': []}}
    with open('test.txt') as f:
        parse(preprocess(f.read()), [mind_map])

    with open('out.mymind', 'w') as f:
        f.write(json.dumps(mind_map))


if __name__ == '__main__':
    main()
