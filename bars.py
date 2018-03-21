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


def get_biggest_bar(json_data):
    return max(json_data["features"], key=lambda feature: 
               feature["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(json_data):
    return min(json_data["features"], key=lambda feature: 
               feature["properties"]["Attributes"]["SeatsCount"])

def get_distance_of_two_points(point_1, point_2):
    return (point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2


def get_closest_bar(json_data, longitude, latitude):
    return min(json_data["features"], key=lambda feature: 
	           get_distance_of_two_points(feature["geometry"]["coordinates"], 
			                              [longitude, latitude]))


if __name__ == '__main__':
    json_data = load_from_json("bars.json")
    smallest_bar = get_smallest_bar(json_data)
    biggest_bar = get_biggest_bar(json_data)
    print("Biggest bar is " + biggest_bar["properties"]["Attributes"]["Name"])
    print("Smallest bar is " + smallest_bar["properties"]["Attributes"]["Name"])
    
    print("Please input your longitude:")
    longitude = float(input())
    print("Please input your latitude:")
    latitude = float(input())
    closest_bar = get_closest_bar(json_data, longitude, latitude)
    print("Closest bar is " + closest_bar["properties"]["Attributes"]["Name"])
