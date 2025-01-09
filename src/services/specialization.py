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
    if found_industry := await industry_curd.get_by_id(  # noqa: F841
        db=db, obj_id=create_schema.industry_id
    ):
        await specialization_crud.create(db=db, create_schema=create_schema)
    raise Exception("Industry not found!")
