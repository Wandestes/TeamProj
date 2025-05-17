import pytest
from config_lib.validator import validate_config

# Схема: config повинен мати поле "name" типу string
schema = {
    "type": "object",
    "properties": {
        "name": { "type": "string" },
        "debug": { "type": "boolean" }
    },
    "required": ["name"],
    "additionalProperties": False
}

def test_valid_config():
    config = {"name": "MyApp", "debug": True}
    assert validate_config(config, schema) == True

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