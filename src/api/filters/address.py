import decimal
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from models import Address


class AddressFilter(Filter):
    country: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None
    home_number: Optional[int] = None
    latitude__gte: Optional[decimal.Decimal] = None
    latitude__lte: Optional[decimal.Decimal] = None
    longitude__gte: Optional[decimal.Decimal] = None
    longitude__lte: Optional[decimal.Decimal] = None

    class Constants(Filter.Constants):
        model = Address
