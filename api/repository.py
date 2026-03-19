from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import URLMap


async def get_url_map(
    short_id: str,
    session: AsyncSession,
    ):
    """Получает запись URLMap по короткому индификатору."""
    result = await session.execute(
        select(URLMap).where(URLMap.short == short_id)
    )
    return result.scalar_one_or_none()

async def counter_transitions(
    url_map: URLMap,
    session: AsyncSession,
    ):
    """Увеличивает колличество переходов по указанной записи URLMap."""
    url_map.count_transitions += 1
    session.add(url_map)
    await session.commit()
