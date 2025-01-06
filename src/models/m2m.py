from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from databases.database import Base


class OrganizationSpecializations(Base):
    """
    Модель м2м связи организации и специализации

    ## Attrs
    - organization_id: int - идентификатор организации
        FK Oraganization
    - specialozation_id: int - идентификатор специялизации
        FK Specialization
    """

    __tablename__ = "organization_specializations"
    __table_args__ = (
        UniqueConstraint(
            "organization_id",
            "specialization_id",
            name="uix_organization_specializations",
        ),
    )

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organization.id", ondelete="CASCADE"),
        primary_key=True,
    )
    specialization_id: Mapped[int] = mapped_column(
        ForeignKey("specialization.id", ondelete="CASCADE"),
        primary_key=True,
    )
