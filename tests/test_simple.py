import pytest

from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.models import URLMap
from api.schemas import CreateUrlMap
from api.services import create_short_url, validate_short_id
from core.basemodel import Base


@pytest.mark.asyncio
async def test_create_short_url():
    """Тест создание короткой ссылки"""
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_session = async_sessionmaker(
        engine, 
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        result = await create_short_url(
            original_url='https://example.com',
            session=session
        )
        assert result.original == 'https://example.com'
        assert result.short is not None
        assert len(result.short) == 6
    await engine.dispose()

@pytest.mark.asyncio
async def test_validate_short_id():
    """Тест проверка валидации"""
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_session = async_sessionmaker(
        engine, 
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        test_url = URLMap(original='https://test.com', short='abc123')
        session.add(test_url)
        await session.commit()
        assert await validate_short_id('abc123', session) is False
        assert await validate_short_id('xyz789', session) is True
    await engine.dispose()

def test_invalid_url():
    """Тест 4: Проверка валидации URL через Pydantic"""
    with pytest.raises(ValidationError):
        CreateUrlMap(original='not-a-url')