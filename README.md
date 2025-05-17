# TeamProj

## Making by:

- Second year student, group ІМ-31 **Shcherbakov Illia** [Telegram](https://t.me/Ilya_net)
- Second year student, group ІМ-31 **Maksymovskyi Nazar** [Telegram](https://t.me/gothicenemy)

# 🛠️ ConfigLib

**ConfigLib** — це Python-бібліотека для завантаження, опису та валідації конфігураційних файлів у форматах YAML та JSON. Вона використовує стандарт JSON Schema для перевірки коректності структури конфігурації.

🔗 **[Design Document](https://docs.google.com/document/d/1fzMnp76GcSN797u70HhqbBeNRQtVZ68fjt3AZxbaSZk/edit?usp=sharing)** — повний опис архітектури, підсистем і рішень.

---

## 🐉 Можливості

- Підтримка YAML та JSON конфігурацій
- Валідація конфігів за допомогою [JSON Schema]
- Простий інтерфейс для інтеграції в інші проєкти
- Покриття юніт-тестами та CI-перевірка на GitHub Actions

---

## ⚙️ Встановлення

```bash
git clone https://github.com/Wandestes/config-lib.git
cd config-lib
pip install -r requirements.txt
```

Або через poetry (якщо використовуєте pyproject.toml):
```
poetry install
```
📚 Приклад використання
```
from config_lib.parser import load_config
from config_lib.schema import load_schema
from config_lib.validator import validate_config

config = load_config("examples/config_example.yaml")
schema = load_schema("examples/schema_example.json")

validate_config(config, schema)

```

▶️ Запуск тестів

Використовуючи pytest та pytest-cov:
```
pytest --cov=config_lib tests/
```

🧐 Структура проєкту
```
config_lib/            # Основна логіка бібліотеки
tests/                 # Юніт-тести
examples/              # Приклади конфігурацій і схем
.github/workflows/     # CI (GitHub Actions)
pyproject.toml         # Конфігурація залежностей
requirements.txt       # Альтернатива для pip
```
🧪 CI
- У репозиторії налаштовано GitHub Actions:
- Автоматичний запуск тестів
- Перевірка покриття коду (coverage)
- Блокування PR, якщо тести не пройдені
