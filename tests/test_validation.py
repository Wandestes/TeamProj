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
    valid, msg = validate_config(config, schema)
    assert valid is True
    assert msg == "Validation passed"

def test_missing_required_field():
    config = {"debug": True}
    valid, msg = validate_config(config, schema)
    assert valid is False
    assert "is a required property" in msg

def test_invalid_type():
    config = {"name": 123, "debug": True}
    valid, msg = validate_config(config, schema)
    assert valid is False
    assert "123 is not of type 'string'" in msg

def test_additional_field_not_allowed():
    config = {"name": "App", "extra": "not allowed"}
    valid, msg = validate_config(config, schema)
    assert valid is False
    assert "Additional properties are not allowed" in msg
