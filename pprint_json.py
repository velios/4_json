import json


def load_data(filepath):
    file = open(filepath, 'r', encoding='utf-8')
    return file.read()


def pretty_print_json(data):
    raw_json_data = json.loads(data)
    return json.dumps(raw_json_data, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    json_data_from_file = load_data('test.json')
    print(pretty_print_json(json_data_from_file))
