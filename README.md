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
**Быстрый старт через Docker**
```bash
docker-compose up --build
```
*Сервис будет доступен по адресу: http://localhost:8000*

*Документация Swagger: http://localhost:8000/docs*

**Автор** 🤝 [Тагаев Мухаммад](https://github.com/Muta-Mad).

**Мой [Telegram](https://t.me/METI_1337)**

