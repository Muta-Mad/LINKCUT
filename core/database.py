from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.settings import settings


engine = create_async_engine(settings.db.url, echo=True)

new_session = async_sessionmaker(
    bind=engine, expire_on_commit=False, autoflush=False, class_=AsyncSession
)


async def get_db():
    """асинхронная функция для получении сессии"""
    async with new_session() as session:
        try:
            yield session
        finally:
            await session.close()
