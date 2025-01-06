from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from constants.industry import (
    MAX_INDUSRTY_NAME_LENGTH,
    MIN_INDUSRTY_NAME_LENGTH,
)
from schemas.paginate import PaginatedResponseBase
from schemas.specialization import SpecializationResponse


class IndustryBase(BaseModel):
    name: str = Field(
        min_length=MIN_INDUSRTY_NAME_LENGTH,
        max_length=MAX_INDUSRTY_NAME_LENGTH,
    )

    class Config:
        from_attributes = True


class IndustryCreate(IndustryBase):
    ...


class IndustryResponse(IndustryBase):
    uid: UUID


class IndustryFullResponse(IndustryResponse):
    uid: UUID
    specializations: List[SpecializationResponse] = []


class IndustryPaginatedResponse(PaginatedResponseBase):
    objects: List[IndustryResponse]
