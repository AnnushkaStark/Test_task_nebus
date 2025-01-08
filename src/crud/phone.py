from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Phone
from schemas.phone import PhoneBase, PhoneCreate

from .async_crud import BaseAsyncCRUD


class PhoneCRUD(BaseAsyncCRUD[Phone, PhoneBase, PhoneCreate]):
    async def get_by_number(
        self, db: AsyncSession, number: str
    ) -> Optional[Phone]:
        statement = select(self.model).where(self.model.number == number)
        result = await db.execute(statement)
        return result.scalars().first()


phone_crud = PhoneCRUD(Phone)
