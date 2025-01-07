from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from crud.industry import industry_curd
from models import Industry


async def check_industry(
    db: AsyncSession, industry_id: int
) -> Optional[Industry]:
    if found_industry := await industry_curd.get_by_id(
        db=db, obj_id=industry_id
    ):
        return found_industry
    raise Exception("Industry not found")
