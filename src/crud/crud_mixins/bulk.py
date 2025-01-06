from typing import Generic, List

from sqlalchemy import delete, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from constants.crud_types import CreateSchemaType, ModelType, UpdateSchemaType


class BulkAsync(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    async def create_bulk(
        self,
        db: AsyncSession,
        *,
        create_schemas: List[CreateSchemaType],
        commit: bool = True,
    ) -> List[ModelType]:
        data = [s.model_dump() for s in create_schemas]
        stmt = insert(self.model).values(data).returning(self.model)
        res = await db.execute(stmt)
        objs = res.scalars().all()
        if commit:
            await db.commit()
        return objs
