from jsonschema import validate as json_validate, ValidationError

def validate_config(config: dict, schema: dict) -> tuple[bool, str]:
    """
    Validate the given configuration dict against a schema dict.
    Returns (True, "Validation passed") if valid,
    otherwise (False, error message).
    """
    try:
        json_validate(instance=config, schema=schema)
        return True, "Validation passed"
    except ValidationError as e:
        return False, str(e)
