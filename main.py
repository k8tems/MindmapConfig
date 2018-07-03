import json


def main():
    root_node = {
        'root': {'id': "hyfkdnca",
                 'text': 'My Mind Map',
                 'layout': 'map',
                 'children': []}}
    with open('out.txt', 'w') as f:
        f.write(json.dumps(root_node))


if __name__ == '__main__':
    main()
