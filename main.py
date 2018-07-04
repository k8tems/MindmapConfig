import json


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


def parse(coordinate_hierarchy):
    """Convert text mind map hierarchy to python data structure"""
    mind_map = []
    node_base = {'children': [], 'id': None, 'side': 'left', 'text': None, 'crd': None}
    root_node = node_base.copy()
    root_node['text'] = 'root'

    for text, (x, y) in coordinate_hierarchy:
        node = node_base.copy()
        node['text'] = text
        node['crd'] = (x, y)
        print(text, x, y)
        parent_candidates = search_parent_candidates(mind_map, (x, y))

        parent = max(parent_candidates, key=lambda x: x['crd'][1]) if parent_candidates else None

        if parent:
            parent['children'].append(node)
        else:
            mind_map.append(node)

    return mind_map


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
