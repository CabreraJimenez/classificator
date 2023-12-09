import json

def read_config(file_path="config/config.json"):
    with open(file_path, "r") as file:
        config = json.load(file)
    return config
