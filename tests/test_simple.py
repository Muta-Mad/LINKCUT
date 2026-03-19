import pytest
import pytest_asyncio
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.models import URLMap
from api.schemas import CreateUrlMap
from api.services import create_short_url, validate_short_id
from core.basemodel import Base


@pytest_asyncio.fixture
async def db_session():
    """Фикстура создаёт тестовую БД в памяти и возвращает сессию"""
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_session = async_sessionmaker(
        engine, 
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session
    await engine.dispose()

@pytest.mark.asyncio
async def test_create_short_url(db_session):
    """Тест Создание короткой ссылки"""
    result = await create_short_url(
        original_url='https://example.com',
        session=db_session
    )
    assert result.original == 'https://example.com'
    assert result.short is not None
    assert len(result.short) == 6

@pytest.mark.asyncio
async def test_validate_short_id(db_session):
    """Тест Проверка валидации ID"""
    test_url = URLMap(original='https://test.com', short='abc123')
    db_session.add(test_url)
    await db_session.commit()
    assert await validate_short_id('abc123', db_session) is False
    assert await validate_short_id('xyz789', db_session) is True


@pytest.mark.asyncio
async def test_create_duplicate_short_id(db_session):
    """Тест проверка уникальности коротких ссылок"""
    result1 = await create_short_url(
        original_url='https://example.com/1',
        session=db_session,
        custom_id='same123'
    )
    assert result1.short == 'same123'
    with pytest.raises(ValueError, match='уже существует'):
        await create_short_url(
            original_url='https://example.com/2',
            session=db_session,
            custom_id='same123'
        )

def test_invalid_url_schema():
    """Тест 4: Проверка валидации URL через Pydantic"""
    with pytest.raises(ValidationError):
        CreateUrlMap(original='not-a-url')
