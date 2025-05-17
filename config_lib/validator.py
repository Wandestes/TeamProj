from jsonschema import validate as json_validate, ValidationError

def validate_config(config: dict, schema: dict) -> tuple[bool, str]:
    try:
        json_validate(instance=config, schema=schema)
        return True, "Validation passed"
    except ValidationError as e:
        return False, f"Validation error: {e.message}"