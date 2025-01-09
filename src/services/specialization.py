from sqlalchemy.ext.asyncio import AsyncSession

from crud.industry import industry_curd
from crud.specialization import specialization_crud
from models import Specialization
from schemas.specialization import SpecializationCreate


async def create(
    db: AsyncSession, create_schema: SpecializationCreate
) -> Specialization:
    create_schema.name = create_schema.name.capitalize()
    if exsisted_name := await specialization_crud.get_by_name(  # noqa: F841
        db=db, name=create_schema.name, industry_id=create_schema.industry_id
    ):
        raise Exception("Specialization alredy exsists")
    found_industry = await industry_curd.get_by_id(
        db=db, obj_id=create_schema.industry_id
    )
    if not found_industry:
        raise Exception("Industry not found!")
    await specialization_crud.create(db=db, create_schema=create_schema)
