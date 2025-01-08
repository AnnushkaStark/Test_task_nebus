import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

from .m2m import OrganizationSpecializations

if TYPE_CHECKING:
    from .address import Address
    from .industry import Industry
    from .phone import Phone
    from .specialization import Specialization


class Organization(Base):
    """
    Модель Организации

    ## Attrs:
        - id: int - идентификатор
        - uid: UUID - идентификатор
        - name: str - название организации
        - industry_id: int - идентификатор отрасли
            в которой работает организация
        - industry: Industry - связь отрасль в которой
            работает орагнизация
        - address: Address - связь с адресом
        - phone_number: List[Phone] - список
            номеров телефонов организации
        - specializations: List[Specialzations] -  связь
            специализации с которыми работает организация

    """

    __tablename__ = "organization"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, unique=True
    )
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String, index=True)
    industry_id: Mapped[int] = mapped_column(
        ForeignKey("industry.id", ondelete="CASCADE")
    )
    industry: Mapped["Industry"] = relationship(
        "Industry", back_populates="organizations"
    )
    address: Mapped["Address"] = relationship(
        "Address", back_populates="organization"
    )
    phone_numbers: Mapped[List["Phone"]] = relationship(
        "Phone", back_populates="organization"
    )
    specializations: Mapped[List["Specialization"]] = relationship(
        "Specialization",
        back_populates="organizations",
        secondary=OrganizationSpecializations.__table__,
    )
