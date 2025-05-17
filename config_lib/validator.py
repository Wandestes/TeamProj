# config_lib/validator.py
from jsonschema import validate as json_validate, ValidationError

def validate_config(config: dict, schema: dict) -> None:
    """
    Validate the given configuration dict against a schema dict.
    Raises ValidationError if invalid.
    """
    json_validate(instance=config, schema=schema)
