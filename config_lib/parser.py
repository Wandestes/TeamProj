import yaml
import json

def load_config(file_path):
    with open(file_path, 'r') as f:
        if file_path.endswith(".yaml") or file_path.endswith(".yml"):
            return yaml.safe_load(f)
        elif file_path.endswith(".json"):
            return json.load(f)
        else:
            raise ValueError("Unsupported config file format")
