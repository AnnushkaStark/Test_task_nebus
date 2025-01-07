from typing import Sequence

from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from models import Organization
from schemas.organization import OrganizationsPaginatedResponse
from utilities.search import get_transliterated_value


class OrganizationSearchCRUD:
    async def get_search_organizations_results(
        self, db: AsyncSession, query: str, skip: int = 0, limit: int = 10
    ) -> OrganizationsPaginatedResponse:
        result = {}
        kwargs = {
            "db": db,
            "query": await get_transliterated_value(query=query),
            "skip": skip,
            "limit": limit,
        }
        result = await self.get_organizations_result(**kwargs)
        return result

    async def get_organizations_result(
        self,
        db: AsyncSession,
        query: list[str],
        skip: int = 0,
        limit: int = 10,
    ) -> Sequence[Organization]:
        statement = (
            select(Organization, func.count().over().label("total"))
            .offset(skip)
            .limit(limit)
            .options(
                joinedload(Organization.industry),
                joinedload(Organization.specializations),
                joinedload(Organization.address),
                joinedload(Organization.phone_numbers),
            )
            .where(*(Organization.name.ilike(f"%{q}%") for q in query))
            .order_by(Organization.name)
        )
        result = await db.execute(statement)
        rows = result.mappings().unique().all()
        return {
            "limit": limit,
            "offset": skip * limit,
            "total": rows[0]["total"] if rows else 0,
            "objects": [r["Organization"] for r in rows],
        }
