from typing import List, Optional

from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from models import Organization

from .address import AddressFilter
from .industry import IndustryFilter


class OrganizationFilter(Filter):
    specializations__in: Optional[List[int]] = []
    specializations__not_in: Optional[List[int]] = []
    industry: IndustryFilter = FilterDepends(
        with_prefix("industry", IndustryFilter)
    )
    address: AddressFilter = FilterDepends(
        with_prefix("address", AddressFilter)
    )

    class Constants(Filter.Constants):
        model = Organization
