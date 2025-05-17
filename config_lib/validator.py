from jsonschema import validate, ValidationError

def validate_config(config: dict, schema: dict) -> None:
    validate(instance=config, schema=schema)
