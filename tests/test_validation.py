# tests/test_validation.py
import pytest
from config_lib.validator import validate_config

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "debug": {"type": "boolean"}
    },
    "required": ["name"],
    "additionalProperties": False
}

def test_valid_config():
    config = {"name": "MyApp", "debug": True}
    validate_config(config, schema)  # повинно пройти без помилок

def test_missing_required_field():
    config = {"debug": True}
    with pytest.raises(Exception):
        validate_config(config, schema)

def test_invalid_type():
    config = {"name": 123, "debug": True}
    with pytest.raises(Exception):
        validate_config(config, schema)

def test_additional_field_not_allowed():
    config = {"name": "App", "extra": "not allowed"}
    with pytest.raises(Exception):
        validate_config(config, schema)
