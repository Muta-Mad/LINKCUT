from pydantic import BaseModel, HttpUrl


class CreateUrlMap(BaseModel):
    """Схема для получения названия ссылок.""" 
    original: HttpUrl
    short: str | None = None


class ReadShortUrl(BaseModel):
    """Схема для выдачи короткой ссылки.""" 
    short: str


class Stats(BaseModel):
    """Схема для возврата колличества переходов.""" 
    count_transitions: int