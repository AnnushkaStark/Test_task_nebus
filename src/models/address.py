import decimal
import uuid
from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

if TYPE_CHECKING:
    from .organization import Organization


class Address(Base):
    """
    Модель адреса

    ## Attrs:
        - id: int - идентификатор
        - uid: UUID - идентификатор
        - country: str - страна
        - region: str - регион
        - city: str - город
        - street: str - улицв
        - home_number: int - номер дома
        - room_number: int - номер офиса
        - latitude: decimal - широта
        - longitude: decimal - долгота
        - organization_id: int - идентификатор организации
            расположенной по данному адресу FK оrganization
        - organization: Organization - связь с организацией
    """

    __tablename__ = "address"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, unique=True
    )
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    country: Mapped[str]
    region: Mapped[str]
    city: Mapped[str]
    street: Mapped[str]
    home_number: Mapped[int]
    room_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    latitude: Mapped[decimal.Decimal]
    longitude: Mapped[decimal.Decimal]
    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organization.id", ondelete="CASCADE")
    )
    organization: Mapped["Organization"] = relationship(
        "Organization", back_populates="address"
    )
