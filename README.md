**LinkCut** — сервис сокращения ссылок 🔗

Сервис для сокращения длинных URL (аналог bitly). Написан на FastAPI с использованием async SQLAlchemy, поддерживает PostgreSQL и SQLite, упакован в Docker.

## 🚀 Возможности:

✂️ Сокращение длинных ссылок

🆔 Поддержка кастомных коротких идентификаторов (опционально)

📊 Статистика переходов по каждой ссылке

🔄 Редирект с короткой ссылки на оригинальную

🗄️ Поддержка PostgreSQL и SQLite

🐳 Полная контейнеризация (Docker + docker-compose)

✅ Unit-тесты на основную логику

🛠️ Стек технологий

    Python 3.12

    FastAPI — веб-фреймворк

    SQLAlchemy 2.0 (async) — ORM

    Alembic — миграции

    PostgreSQL / SQLite — базы данных

    Pydantic — валидация данных

    Docker + docker-compose — контейнеризация

    pytest — тестирование
**📦 Установка и запуск**
## Локальный запуск
1 - Клонировать репозиторий:
```bash
git clone https://github.com/Muta-Mad/LINKCUT.git
cd LINKCUT
```
2 - Создать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```
3 - Установить зависимости:
```bash
pip install -r requirements.txt
```
4 - Создать файл .env (пример в .env.example)
5 - Применить миграции:
```bash
alembic upgrade head
```
6 - Запустить сервер:
```bash
uvicorn main:app --reload
```
*Сервис будет доступен по адресу: http://localhost:8000*

*Документация Swagger: http://localhost:8000/docs*

**Запуск через Docker**
```bash
docker-compose up --build
```
**[Автор](https://github.com/Muta-Mad)** 🤝 Тагаев Мухаммад.

**Мой [Telegram](https://t.me/METI_1337)**

