import decimal

from pydantic import BaseModel


class AddressBase(BaseModel):
    country: str
    region: str
    city: str
    street: str
    home_number: int
    room_number: int
    latitude: decimal.Decimal
    longitude: decimal.Decimal

    class Config:
        from_attributes = True


class AddressCreate(AddressBase):
    ...


class AddressCreateDB(AddressCreate):
    organization_id: int


class AddressResponse(AddressBase):
    ...
