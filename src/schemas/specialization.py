from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from constants.specialization import (
    MAX_SPECIALIZATION_NAME_LENGTH,
    MIN_SPECIALIZATION_NAME_LENGTH,
)
from schemas.paginate import PaginatedResponseBase


class SpecializationBase(BaseModel):
    name: str = Field(
        min_length=MIN_SPECIALIZATION_NAME_LENGTH,
        max_length=MAX_SPECIALIZATION_NAME_LENGTH,
    )

    class Config:
        from_attributes = True


class SpecializationCreate(SpecializationBase):
    industry_id: int


class SpecializationCreateDB(SpecializationCreate):
    ...


class SpecializationResponse(SpecializationBase):
    id: int
    uid: UUID


class SpecializationPaginatedResponse(PaginatedResponseBase):
    objects: List[SpecializationResponse] = []
