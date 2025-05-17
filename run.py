from config_lib import load_config, load_schema, validate_config

def main():
    config = load_config("examples/config_example.yaml")
    schema = load_schema("examples/schema_example.json")
    valid, message = validate_config(config, schema)
    print(message)

if __name__ == "__main__":
    main()
