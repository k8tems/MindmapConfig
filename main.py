import json


def split_indent(line):
    num_spaces = 0
    for l in line:
        if l != ' ':
            break
        num_spaces += 1
    return line[num_spaces:], num_spaces // 4


def parse(text):
    """Convert text mind map hierarchy to python data structure"""
    for line in text.split('\n'):
        line, indent_level = split_indent(line)


def main():
    mind_map = {
        'root': {'id': "hyfkdnca",
                 'text': 'My Mind Map',
                 'layout': 'map',
                 'children': None}}
    with open('test.txt') as f:
        mind_map['children'] = parse(f.read())

    with open('out.mymind', 'w') as f:
        f.write(json.dumps(mind_map))


if __name__ == '__main__':
    main()
