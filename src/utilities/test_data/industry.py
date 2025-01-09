from sqlalchemy.ext.asyncio import AsyncSession

from schemas.industry import IndustryCreate
from services import industry as industry_service


async def create_test_industryies(db: AsyncSession) -> None:
    industries = [
        IndustryCreate(name="Гастрономия"),
        IndustryCreate(name="Moда"),
        IndustryCreate(name="Дизайн"),
    ]
    try:
        for industry in industries:
            await industry_service.create(db=db, create_data=industry)
    except Exception as e:
        raise Exception(str(e))
