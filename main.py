import json


def parse(text):
    pass


def main():
    root_node = {
        'root': {'id': "hyfkdnca",
                 'text': 'My Mind Map',
                 'layout': 'map',
                 'children': []}}
    with open('test.txt') as f:
        parse(f.read())
    with open('out.mymind', 'w') as f:
        f.write(json.dumps(root_node))


if __name__ == '__main__':
    main()
