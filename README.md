# Запуск приложения



Для начала мы заходим в директорию backend
```
cd .\.backend\
```

Устанавливаем виртуальное окружение
```
python -m venv .venv
```

Активируем виртуальное окружение
```
.\.venv\Scripts\activate
```

Устанавливаем poetry
```
pip install poetry
```

Устанавливаем все зависимости
```
poetry install
```

Активируем сервера разработки
```
poetry run python -m src
```

Миграции
```    
alembic -c src/adapters/database/alembic.ini revision --autogenerate -m "name"
alembic -c src/adapters/database/alembic.ini upgrade head
```