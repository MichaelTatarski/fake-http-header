import json


def load_dict(json_file) -> dict:
    json_acceptable_string = json_file.replace("'", '"')
    return json.loads(json_acceptable_string)
