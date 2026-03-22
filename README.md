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
<img width="870" height="619" alt="Image" src="https://github.com/user-attachments/assets/7329342f-cf3e-4d9d-82ba-3619558d688f" />

Логин и получение JWT
<img width="869" height="592" alt="Image" src="https://github.com/user-attachments/assets/7f5b99a6-75a9-4c54-a559-a5da91dd0344" />
(Неверный логин или пароль)
<img width="869" height="615" alt="Image" src="https://github.com/user-attachments/assets/86a3cbf3-d28d-4f1c-b825-584b877e63f6" />

Авторизация через Swagger
<img width="650" height="582" alt="Image" src="https://github.com/user-attachments/assets/86706f87-b139-42b1-91b5-75f472423fcd" />
<img width="647" height="437" alt="Image" src="https://github.com/user-attachments/assets/9bdfab4d-a9cd-4e14-b37c-88334fa1a04f" />

Вызов POST /chat
<img width="867" height="723" alt="Image" src="https://github.com/user-attachments/assets/dbfa710b-3509-4fb5-b9bd-4c0c0ac59bca" />

Получение истории через GET /chat/history
<img width="866" height="872" alt="Image" src="https://github.com/user-attachments/assets/44d9bb96-7f44-4442-8861-d29093982825" />

Удаление истории через DELETE /chat/history
<img width="867" height="459" alt="Image" src="https://github.com/user-attachments/assets/b2ffd824-1b13-474c-b0d9-c0ecdfadc640" />
<img width="884" height="546" alt="Image" src="https://github.com/user-attachments/assets/b69aa934-b923-4d6d-a2d5-a8aae3746c4b" />
