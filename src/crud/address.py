from models import Address
from schemas.address import AddressBase, AddressCreate

from .async_crud import BaseAsyncCRUD


class AddressCRUD(BaseAsyncCRUD[Address, AddressBase, AddressCreate]):
    pass


address_crud = AddressCRUD(Address)
