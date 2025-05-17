from jsonschema import validate, ValidationError

def validate_config(config, schema):
    try:
        validate(instance=config, schema=schema)
        return True, "Validation passed"
    except ValidationError as e:
        return False, f"Validation error: {e.message}"
