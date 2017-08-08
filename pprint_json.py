import json
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as data_file:
        return data_file.read()


def pretty_print_json(input_json_data):
    unformatted_json_data = json.loads(input_json_data)
    pretty_printed_json_data = json.dumps(unformatted_json_data, sort_keys=True, indent=4,
                                          separators=(',', ': '), ensure_ascii=False)
    print(pretty_printed_json_data)


if __name__ == '__main__':
    parser_description = """
    Скрипт на вход принимает путь до файла в котором
    хранится JSON и выводит его содержимое в консоль в удобном для чтении виде.
    Файл для примера можно скачать на https://data.mos.ru/
    """
    cmd_argument_parser = argparse.ArgumentParser(description=parser_description)
    cmd_argument_parser.add_argument('filepath', help='Имя файла с неформатированным JSON', type=str)
    cmd_arguments = cmd_argument_parser.parse_args()
    json_data_from_file = load_data(cmd_arguments.filepath)
    pretty_print_json(json_data_from_file)
