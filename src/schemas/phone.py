from pydantic import BaseModel


class PhoneBase(BaseModel):
    number: str

    class Config:
        from_attributes = True


class PhoneCreate(PhoneBase):
    ...


class PhoneCreateDB(PhoneCreate):
    organization_id: int


class PhoneResponse(PhoneBase):
    ...
