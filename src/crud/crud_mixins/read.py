from typing import Generic, Optional, Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from constants.crud_types import ModelType


class ReadAsync(Generic[ModelType]):
    async def get_by_id(
        self, db: AsyncSession, *, obj_id: int
    ) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.id == obj_id)
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_by_uid(
        self, db: AsyncSession, *, uid: UUID
    ) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.uid == uid)
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_multi_by_ids(
        self, db: AsyncSession, *, ids: list[int]
    ) -> Sequence[ModelType]:
        if not ids:
            return []
        statement = select(self.model).where(self.model.id.in_(ids))
        result = await db.execute(statement)
        objects = result.scalars().all()
        result = Sequence(objects)
        result.model = self.model
        return result
