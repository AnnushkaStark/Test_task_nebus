import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

if TYPE_CHECKING:
    from .organization import Organization
    from .specialization import Specialization


class Industry(Base):
    """
    Модель отрасли

    ## Attrs:
        - id: int - идентификатор
        - uid: UUID - идентификатор
        - name: str - название
        - specializations: Specializations -
            связь специализации отрасли
        - organizations: Organizations связь организации
            в этой отрасли
    """

    __tablename__ = "industry"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, unique=True
    )
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String, index=True, unique=True)
    specializations: Mapped[List["Specialization"]] = relationship(
        "Specialization", back_populates="industry"
    )
    organizations: Mapped[List[Organization]] = relationship(
        "Organization", back_populates="industry"
    )
