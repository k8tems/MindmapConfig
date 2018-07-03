import json


def parse(text):
    return {'a': ['b'], 'c': ['d']}


def convert(parsed):
    """Convert mind map hierarchy to a output format"""
    pass


def main():
    mind_map = {
        'root': {'id': "hyfkdnca",
                 'text': 'My Mind Map',
                 'layout': 'map',
                 'children': None}}
    with open('test.txt') as f:
        mind_map['children'] = convert(parse(f.read()))

    with open('out.mymind', 'w') as f:
        f.write(json.dumps(mind_map))


if __name__ == '__main__':
    main()
