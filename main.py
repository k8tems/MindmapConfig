import json


def parse(text):
    """Convert text mind map hierarchy to python data structure"""
    return [{'a': ['b']}, {'c': ['d']}]


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
