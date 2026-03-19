from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from core.basemodel import Base
from core.idmixin import IdPkMixin
from core.constants import SHORT_LENGTH, MAX_LENGTH, DEFAULT_COUNT


class URLMap(IdPkMixin, Base):
    """Модель для хранения соответвия между оригинальными и короткими ссылками."""
    __tablename__ = 'url_maps'
    original: Mapped[str] = mapped_column(String(length=MAX_LENGTH))
    short: Mapped[str] = mapped_column(String(length=SHORT_LENGTH), unique=True)
    count_transitions: Mapped[int] = mapped_column(default=DEFAULT_COUNT)
