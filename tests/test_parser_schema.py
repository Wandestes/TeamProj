import pytest
from config_lib.parser import load_config
from config_lib.schema import load_schema
import tempfile
import json
import os

def test_load_config_yaml(tmp_path):
    yaml_content = """
name: TestApp
debug: true
"""
    yaml_file = tmp_path / "config.yaml"
    yaml_file.write_text(yaml_content)

    config = load_config(str(yaml_file))
    assert isinstance(config, dict)
    assert config["name"] == "TestApp"
    assert config["debug"] is True

def test_load_config_json(tmp_path):
    json_content = {
        "name": "TestApp",
        "debug": True
    }
    json_file = tmp_path / "config.json"
    with open(json_file, "w") as f:
        json.dump(json_content, f)

    config = load_config(str(json_file))
    assert isinstance(config, dict)
    assert config["name"] == "TestApp"
    assert config["debug"] is True

def test_load_config_unsupported_extension(tmp_path):
    txt_file = tmp_path / "config.txt"
    txt_file.write_text("some text")

    with pytest.raises(ValueError):
        load_config(str(txt_file))

def test_load_schema_json(tmp_path):
    schema_content = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "debug": {"type": "boolean"}
        },
        "required": ["name"],
        "additionalProperties": False
    }
    schema_file = tmp_path / "schema.json"
    with open(schema_file, "w") as f:
        json.dump(schema_content, f)

    schema = load_schema(str(schema_file))
    assert isinstance(schema, dict)
    assert "properties" in schema
    assert "name" in schema["properties"]
    assert "debug" in schema["properties"]
