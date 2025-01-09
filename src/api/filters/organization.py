from typing import List, Optional, Sequence

from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from models import Address, Industry, Organization, Specialization

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

    async def filter(
        self, db: AsyncSession, skip: int = 0, limit: int = 20
    ) -> Sequence[Organization]:
        statement = (
            select(Organization, func.count().over().label("total"))
            .options(
                selectinload(Organization.address),
                selectinload(Organization.phone_numbers),
                selectinload(Organization.industry),
                selectinload(Organization.specializations),
            )
            .offset(skip)
            .limit(limit)
            .order_by(Organization.name)
        )
        if (
            self.specializations__in is not None
            and self.specializations__in != []
        ):
            statement = statement.filter(
                Organization.specializations.any(
                    Specialization.id.in_(self.specializations__in)
                )
            )
        if (
            self.specializations__not_in is not None
            and self.specializations__not_in != []
        ):
            statement = statement.filter(
                ~Organization.specializations.any(
                    Specialization.id.in_(self.specializations__not_in)
                )
            )
        if self.industry is not None:
            filter_industry = self.industry
            if (
                hasattr(filter_industry, "name")
                and filter_industry.name is not None
            ):
                statement = statement.join(Industry)
                statement = statement.where(
                    Industry.name == filter_industry.name
                )
        if self.address is not None:
            filter_address = self.address
            if (
                hasattr(filter_address, "country")
                and filter_address.country is not None
            ):
                statement = statement.join(Address)
                statement = statement.where(
                    Address.country == filter_address.country
                )
            if (
                hasattr(filter_address, "region")
                and filter_address.region is not None
            ):
                statement = statement.join(Address)
                statement = statement.where(
                    Address.region == filter_address.region
                )
            if (
                hasattr(filter_address, "street")
                and filter_address.street is not None
            ):
                statement = statement.join(Address)
                statement = statement.where(
                    Address.street == filter_address.street
                )
            if (
                hasattr(filter_address, "home_number")
                and filter_address.home_number is not None
            ):
                statement = statement.join(Address)
                statement = statement.where(
                    Address.home_number == filter_address.home_number
                )
            if (
                hasattr(filter_address, "latitude__gte")
                and filter_address.latitude__gte is not None
            ):
                statement = statement.join(Address)
                statement = statement.where(
                    Address.latitude >= filter_address.latitude__gte
                )
            if (
                hasattr(filter_address, "latitude__lte")
                and filter_address.latitude__lte is not None
            ):
                statement = statement.join(Address)
                statement = statement.where(
                    Address.latitude <= filter_address.latitude__lte
                )
            if (
                hasattr(filter_address, "longitude__gte")
                and filter_address.longitude__gte is not None
            ):
                statement = statement.join(Address)
                statement = statement.where(
                    Address.longitude >= filter_address.longitude__gte
                )
            if (
                hasattr(filter_address, "longitude__lte")
                and filter_address.longitude__lte is not None
            ):
                statement = statement.join(Address)
                statement = statement.where(
                    Address.longitude <= filter_address.longitude__lte
                )
        result = await db.execute(statement)
        rows = result.mappings().unique().all()
        return {
            "limit": limit,
            "offset": skip * limit,
            "total": rows[0]["total"] if rows else 0,
            "objects": [r["Organization"] for r in rows],
        }
