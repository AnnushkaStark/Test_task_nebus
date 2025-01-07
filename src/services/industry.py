from sqlalchemy.ext.asyncio import AsyncSession

from crud.industry import industry_curd
from models import Industry
from schemas.industry import IndustryCreate


async def create(db: AsyncSession, create_data: IndustryCreate) -> Industry:
    create_data.name = create_data.name.capitalize()
    if exsisted_industry := await industry_curd.get_by_name(  # noqa: F841
        db=db, name=create_data.name
    ):
        raise Exception("Industry alredy exsists!")
    return await industry_curd.create(db=db, create_schema=create_data)
