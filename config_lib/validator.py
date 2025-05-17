import jsonschema


def validate_config(config: dict, schema: dict) -> bool:
    """
    Перевіряє відповідність конфігурації схемі.

    :param config: Дані конфігурації
    :param schema: JSON-схема для валідації
    :return: True, якщо валідна, інакше викликає виняток
    """
    jsonschema.validate(instance=config, schema=schema)
    return True