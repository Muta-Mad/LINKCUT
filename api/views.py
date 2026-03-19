from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from api.repository import counter_transitions, get_url_map
from api.schemas import CreateUrlMap, ReadShortUrl, Stats
from api.services import create_short_url
from core.database import get_db

router = APIRouter()

@router.post('/shorten', response_model=ReadShortUrl, status_code=status.HTTP_201_CREATED)
async def shorten(
    data: CreateUrlMap,
    session: AsyncSession = Depends(get_db),
):
    """Принимает длинную ссылку, возвращает короткий идентификатор."""
    result = await create_short_url(
        original_url=str(data.original), 
        custom_id=data.short, 
        session=session
    )
    return ReadShortUrl(short=result.short)

@router.get('/{short_id}')
async def redirect_short_link(
    short_id: str,
    session: AsyncSession = Depends(get_db),
    ):
    """Редиректит на оригинальную ссылку."""
    url_map = await get_url_map(short_id, session)
    if not url_map:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Не найдена ссылка!'
        )
    await counter_transitions(url_map, session)
    return RedirectResponse(url=str(url_map.original))

@router.get('/stats/{short_id}', response_model=Stats)
async def get_stats(
    short_id: str,
    session: AsyncSession = Depends(get_db),
):
    """Возвращает количество переходов."""
    url_map = await get_url_map(short_id, session)
    if not url_map:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Не найдена ссылка!'
        )
    return Stats(count_transitions=url_map.count_transitions)
