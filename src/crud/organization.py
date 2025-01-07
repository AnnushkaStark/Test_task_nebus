from typing import Optional
from uuid import UUID

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from models import Organization
from schemas.organization import (
    OrganizationBase,
    OrganizationCreate,
    OrganizationCreateDB,
)

from .async_crud import BaseAsyncCRUD


class OrganizationCRUD(
    BaseAsyncCRUD[Organization, OrganizationBase, OrganizationCreate]
):
    async def get_by_uid(
        self, db: AsyncSession, *, uid: UUID
    ) -> Optional[Organization]:
        statament = (
            select(self.model)
            .options(
                joinedload(self.model.address),
                joinedload(self.model.phone_numbers),
                joinedload(self.model.industry),
                joinedload(self.model.specializations),
            )
            .where(self.model.uid == uid)
        )
        result = await db.execute(statament)
        return result.scalars().unique().first()

    async def create(
        self,
        db: AsyncSession,
        create_schema: OrganizationCreateDB,
        commit: bool = True,
    ) -> Organization:
        data = create_schema.model_dump(exclude_unset=True)
        stmt = (
            insert(self.model)
            .values(**data)
            .returning(self.model)
            .options(
                selectinload(self.model.address),
                selectinload(self.model.phone_numbers),
                selectinload(self.model.industry),
                selectinload(self.model.specializations),
            )
        )
        res = await db.execute(stmt)
        if commit:
            await db.commit()
        return res.scalars().first()


organization_crud = OrganizationCRUD(Organization)
