import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

if TYPE_CHECKING:
    from .organization import Organization


class Phone(Base):
    """
    Модель телефонного номера

    ## Attrs:
        - id : int - идентификатор
        - uid: UUID - идентфикатор
        - number: str - номер телефона
        - organization_id: int - идентификатор организации
            которой принадлежит номер FK Organization
        - organization: Organization - связь с организацией
    """

    __tablename__ = "phone"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, unique=True
    )
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    number: Mapped[str] = mapped_column(String, unique=True)
    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organization.id", ondelete="CASCADE")
    )
    organization: Mapped["Organization"] = relationship(
        "Organization", back_populates="phone_numbers"
    )
