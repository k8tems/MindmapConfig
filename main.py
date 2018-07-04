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
    candidates = candidates or []

    for node in mind_map:
        candidates += search_parent_candidates(node['children'], crd, candidates)
        node_x, node_y = node['crd']
        if crd[0] - node_x == 1 and node_y < crd[1]:
            candidates.append(node)

    return candidates


def elect(candidates):
    return max(candidates, key=lambda x: x['crd'][1]) if candidates else None


def remove_crds(mind_map):
    for node in mind_map:
        remove_crds(node['children'])
        del node['crd']
    return mind_map


def parse(coordinate_hierarchy):
    """Convert text mind map hierarchy to python data structure"""
    mind_map = []
    node_base = {'children': [], 'id': None, 'side': 'left', 'text': None, 'crd': None}

    for text, (x, y) in coordinate_hierarchy:
        node = deepcopy(node_base)
        node['text'] = text
        # Add coordinate information to simplify the search process
        # Should be cleaned up with `remove_crds` prior to returning
        node['crd'] = (x, y)
        parent = elect(search_parent_candidates(mind_map, (x, y)))

        if parent:
            parent['children'].append(node)
        else:
            mind_map.append(node)

    return remove_crds(mind_map)


def get_indent_hierarchy(text):
    """
    Convert text mind map hierarchy to a list of tuples
    consisting of the indent level and node text
    """
    return [split_indent(line) for line in text.split('\n')]


def get_coordinate_hierarchy(indent_hierarchy):
    return [(line, (num_indent, i)) for i, (line, num_indent) in enumerate(indent_hierarchy)]


def main():
    mind_map = {
        'root': {'id': "hyfkdnca",
                 'text': 'My Mind Map',
                 'layout': 'map',
                 'children': None}}
    with open('test.txt') as f:
        mind_map['children'] = parse(get_coordinate_hierarchy(get_indent_hierarchy(f.read())))

    with open('out.mymind', 'w') as f:
        f.write(json.dumps(mind_map))


if __name__ == '__main__':
    main()
