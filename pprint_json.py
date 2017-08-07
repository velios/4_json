import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as data_file:
        return data_file.read()


def pretty_print_json(input_json_data):
    unformatted_json_data = json.loads(input_json_data)
    pretty_printed_json_data = json.dumps(unformatted_json_data, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    print(pretty_printed_json_data)


if __name__ == '__main__':
    json_data_from_file = load_data('test.json')
    pretty_print_json(json_data_from_file)
