import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

from .m2m import OrganizationSpecializations

if TYPE_CHECKING:
    from .industry import Industry
    from .organization import Organization


class Specialization(Base):
    """
    Модель специализации

    ## Attrs:
        -id: int - идентификатор
        - uid: UUID - идентификатор
        - name: str - название
        - industry_id: int - идентфикатор сферы
        деятельности к которой относится специялизация организации
        (FK Industry)
        - industry: Industry - связь с сферой деятельности
        - organizations: List[Organizations] - связь м2м
            организации относящиеся к этой специалзации
    """

    __tablename__ = "specialization"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, unique=True
    )
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String, index=True, unique=True)
    industry_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("indusrty.id", ondelete="CASCADE")
    )
    industry: Mapped["Industry"] = relationship(
        "Industry", back_populates="specializations"
    )
    organizations = Mapped[List["Organization"]] = relationship(
        "Organization",
        back_populates="specializations",
        secondary=OrganizationSpecializations.__table__,
    )
