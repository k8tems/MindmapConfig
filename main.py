import json


def split_indent(line):
    num_spaces = 0
    for l in line:
        if l != ' ':
            break
        num_spaces += 1
    assert(num_spaces % 4 == 0)
    return line[num_spaces:], num_spaces // 4


def parse(indent_hierarchy):
    """Convert text mind map hierarchy to python data structure"""
    mind_map = []
    node_base = {'children': [], 'id': None, 'side': 'left', 'text': None}
    for line, num_indent in indent_hierarchy:
        node = node_base.copy()
        node['text'] = line
        mind_map.append(node)
    return mind_map


def get_indent_hierarchy(text):
    """
    Convert text mind map hierarchy to a list of tuples
    consisting of the indent level and node text
    """
    return [split_indent(line) for line in text.split('\n')]


def main():
    mind_map = {
        'root': {'id': "hyfkdnca",
                 'text': 'My Mind Map',
                 'layout': 'map',
                 'children': None}}
    with open('test.txt') as f:
        mind_map['children'] = parse(get_indent_hierarchy(f.read()))

    with open('out.mymind', 'w') as f:
        f.write(json.dumps(mind_map))


if __name__ == '__main__':
    main()
