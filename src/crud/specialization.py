from typing import Optional, Sequence

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Specialization
from schemas.specialization import SpecializationBase, SpecializationCreate

from .async_crud import BaseAsyncCRUD


class SpecializationCRUD(
    BaseAsyncCRUD[Specialization, SpecializationBase, SpecializationCreate]
):
    async def get_by_name_and_industry_id(
        self, db: AsyncSession, name: str, industry_id: int
    ) -> Optional[Specialization]:
        statement = select(self.model).where(
            self.model.name == name, self.model.industry_id == industry_id
        )
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_by_name_and_industry_id(
        self, db: AsyncSession, name: str, industry_id: int
    ) -> Optional[Specialization]:
        statement = select(self.model).where(self.model.name == name)
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_mullti_with_total_by_industry_id(
        self,
        db: AsyncSession,
        industry_id: int,
        skip: int = 0,
        limit: int = 1000,
    ) -> Sequence[Specialization]:
        statement = (
            select(self.model, func.count().over().label("total"))
            .offset(skip)
            .limit(limit)
            .where(self.model.industry_id == industry_id)
            .order_by(self.model.name)
        )
        result = await db.execute(statement)
        rows = result.mappings().unique().all()
        return {
            "limit": limit,
            "offset": skip * limit,
            "total": rows[0]["total"] if rows else 0,
            "objects": [r["Specialization"] for r in rows],
        }


specialization_crud = SpecializationCRUD(Specialization)
