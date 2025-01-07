from models import Phone
from schemas.phone import PhoneBase, PhoneCreate

from .async_crud import BaseAsyncCRUD


class PhoneCRUD(BaseAsyncCRUD[Phone, PhoneBase, PhoneCreate]):
    pass


phone_crud = PhoneCRUD(Phone)
