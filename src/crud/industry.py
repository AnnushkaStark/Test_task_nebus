from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from models import Industry
from schemas.industry import IndustryBase, IndustryCreate

from .async_crud import BaseAsyncCRUD


class IndustryCRUD(BaseAsyncCRUD[Industry, IndustryBase, IndustryCreate]):
    async def get_by_name(
        self, db: AsyncSession, name: str
    ) -> Optional[Industry]:
        statement = select(self.model).where(self.model.name == name)
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_multi_with_total(
        self, db: AsyncSession, skip: int = 0, limit: int = 1000
    ) -> Sequence[Industry]:
        statement = (
            select(self.model, func.count().over().label("total"))
            .offset(skip)
            .limit(limit)
            .options(joinedload(self.model.specializations))
            .order_by(self.model.name)
        )
        result = await db.execute(statement)
        rows = result.mappings().unique().all()
        return {
            "limit": limit,
            "offset": skip * limit,
            "total": rows[0]["total"] if rows else 0,
            "objects": [r["Industry"] for r in rows],
        }

    async def get_by_uid(
        self, db: AsyncSession, uid: UUID
    ) -> Optional[Industry]:
        statement = (
            select(self.model)
            .options(joinedload(self.model.specializations))
            .where(self.model.uid == uid)
        )
        result = await db.execute(statement)
        return result.scalars().unique().first()


industry_curd = IndustryCRUD(Industry)
