from pydantic import BaseModel, HttpUrl, Field, field_validator

from core.constants import MAX_LENGTH, SHORT_LENGTH

class CreateUrlMap(BaseModel):
    """Схема для получения названия ссылок.""" 
    original: HttpUrl
    short: str | None = Field(None, max_length=SHORT_LENGTH)

    @field_validator('original')
    @classmethod
    def check_length(cls, value: HttpUrl):
        if len(str(value)) > MAX_LENGTH:
            raise ValueError(
                f'URL слишком длинный, максимально {MAX_LENGTH} символов'
            )
        return value


class ReadShortUrl(BaseModel):
    """Схема для выдачи короткой ссылки.""" 
    short: str


class Stats(BaseModel):
    """Схема для возврата количества переходов.""" 
    count_transitions: int
