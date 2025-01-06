from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from constants.organization import (
    MAX_OTGANIZATION_NAME_LENGTH,
    MIN_ORGANIZATION_NAME_LENGTH,
)
from schemas.address import AddressCreate, AddressResponse
from schemas.industry import IndustryResponse
from schemas.paginate import PaginatedResponseBase
from schemas.phone import PhoneCreate, PhoneResponse
from schemas.specialization import SpecializationResponse


class OrganizationBase(BaseModel):
    name: str = Field(
        min_length=MIN_ORGANIZATION_NAME_LENGTH,
        MAX_OTGANIZATION_NAME_LENGTH=MAX_OTGANIZATION_NAME_LENGTH,
    )

    class Config:
        from_attributes = True


class OrganizationCreate(OrganizationBase):
    address: AddressCreate
    phone_numbers: List[PhoneCreate] = []
    industry_id: int
    specializations: List[int] = []


class OrganizationCreateDB(OrganizationBase):
    ...


class OrganizationResponse(OrganizationBase):
    id: int
    uid: UUID
    address: AddressResponse
    phone_numbers: List[PhoneResponse] = []
    industry: IndustryResponse
    specializations: List[SpecializationResponse] = []


class OrganizationsPaginatedResponse(PaginatedResponseBase):
    objects: List[OrganizationResponse]
