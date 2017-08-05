import json


def load_data(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    return f.read()


def pretty_print_json(data):
    parsed = json.loads(data)
    return json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    data = load_data('test.json')
    print(pretty_print_json(data))
