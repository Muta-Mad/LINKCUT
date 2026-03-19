import random
import string

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import URLMap
from core.constants import MAX_ITERATION, SHORT_ID_LENGTH


async def create_short_url(
    original_url: str,
    session: AsyncSession,
    custom_id: str | None = None,
    ):
    """Создает короткую ссылку."""
    if not custom_id:
        custom_id = await get_unique_short_id(session)
    is_valid = await validate_short_id(custom_id, session)
    if not is_valid:
        raise ValueError('Предложенный вариант короткой ссылки уже существует.')
    url_map = URLMap(original=original_url, short=custom_id)
    session.add(url_map)
    await session.commit()
    return url_map
    
async def get_unique_short_id(session: AsyncSession):
    """Генерирует уникальный короткий идентификатор."""
    chars = string.ascii_letters + string.digits
    for _ in range(MAX_ITERATION):
        short = ''.join(random.choices(chars, k=SHORT_ID_LENGTH))
        if await validate_short_id(short, session):
            return short
    raise ValueError(f'Не удалось сгенерировать уникальный ID после {MAX_ITERATION} попыток')

async def validate_short_id(
    short_id: str,
    session: AsyncSession):
    """Проверяет, можно ли использовать short_id."""
    return not (
        await session.execute(
            select(URLMap).where(
                URLMap.short == short_id
            )
        )
    ).scalar_one_or_none()
