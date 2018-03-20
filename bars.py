import json
import codecs

def load_data(filepath):
    text = None
    try:
        with codecs.open(filepath, "r", "utf_8_sig") as loading_file:
            return loading_file.read()
    except FileNotFoundError as ex:
        print(ex)


def load_from_json(filepath):
    try:
        with codecs.open(filepath, "r", "utf_8_sig") as loading_file:
            return json.load(loading_file)
    except FileNotFoundError as ex:
        print(ex)


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    json_data = load_from_json("bars.json")
    print(json_data)
