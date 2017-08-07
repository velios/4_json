# Prettify JSON

Learning project. Make pretty JSON output.

# Quickstart

Just take some JSON file to utility and get the pretty JSON output.

The site data.mos.ru has many different data, including a <a href="https://data.mos.ru/opendata/7710881420-bary">list of Moscow bars</a>. It can be downloaded in json format.

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>
# Add the file you want to prettify and you'll get a nice JSON output like this

{'4': 5, '6': 7}
after use =>
{
    "4": 5,
    "6": 7
}

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
