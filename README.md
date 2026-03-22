# Построение защищённого API для работы с большой языковой моделью

FastAPI серверное приложение, предоставляющее защищённый API для взаимодействия с большой языковой моделью через сервис OpenRouter

## Установка
Перед установкой, убедитесь, что у вас установлен Python, склонируйте репозиторий с помощью команды:
git clone https://github.com/Seeneld/project3_priezzhikh_timofey_M25-555.git

Переход в папку проетка
cd project3_priezzhikh_timofey_M25-555.git

Установка uv
pip install uv

Инициализация проекта
uv init 

Создание виртуального окружения
uv venv

Активировация виртуального окружения
MacOS/Linux: source .venv/bin/activate
Windows: .venv\Scripts\activate.batWindows

Установка зависимостей проекта
uv pip install -r <(uv pip compile pyproject.toml)

Зарегистрируйтесь на платформе OpenRouter и получите API-ключ. Вставьте его в файл .env в корне проекта в строку OPENROUTER_API_KEY="Ваш API-ключ"

Запуск приложения
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Переход по ссылке
http://127.0.0.1:8000/docs

## Демонстрация работы

Регистрация пользователя


Логин и получение JWT


Авторизация через Swagger


Вызов POST /chat


Получение истории через GET /chat/history


Удаление истории через DELETE /chat/history
