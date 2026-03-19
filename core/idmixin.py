from sqlalchemy.orm import Mapped, mapped_column


class IdPkMixin:
    """Мексин ID"""
    id: Mapped[int] = mapped_column(primary_key=True)